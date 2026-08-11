import os
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
DEFAULT_MODEL="openai/gpt-oss-20b:free"
api_key = os.getenv("OPENAI_API_KEY")
# Initialize the OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# 1. Define a small text set (our knowledge base)
documents = [
    "The cat is sleeping on the sunny porch.",
    "A golden retriever is chasing a frisbee in the park.",
    "The stock market experienced a significant drop today due to inflation fears.",
    "Python is a versatile programming language widely used in AI and data science.",
    "To bake a chocolate cake, you need flour, sugar, eggs, and cocoa powder."
]

def get_embedding(text, model="text-embedding-3-small"):
    """Fetches the embedding vector for a given text from OpenAI."""
    # It's best practice to replace newlines with spaces for embeddings
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def cosine_similarity(vec_a, vec_b):
    """Calculates the cosine similarity between two vectors."""
    a = np.array(vec_a)
    b = np.array(vec_b)
    # Cosine similarity formula: (A · B) / (||A|| * ||B||)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def main():
    print("Generating embeddings for the document set... (this takes a moment)\n")
    # 2. Generate and store embeddings for all documents
    doc_embeddings = [get_embedding(doc) for doc in documents]

    # 3. Define the semantic query
    query = "Tell me about coding and software development."
    print(f"🔍 Search Query: '{query}'\n")

    # 4. Generate the embedding for the user's query
    query_embedding = get_embedding(query)

    # 5. Calculate similarity scores between the query and each document
    results = []
    for i, doc_emb in enumerate(doc_embeddings):
        score = cosine_similarity(query_embedding, doc_emb)
        results.append((score, documents[i]))

    # 6. Sort the results so the highest similarity score is at the top
    results.sort(key=lambda x: x[0], reverse=True)

    # 7. Print the ranked results
    print("📊 Search Results (Ranked by Semantic Similarity):")
    print("-" * 60)
    for rank, (score, text) in enumerate(results, start=1):
        # We format the score to 4 decimal places for readability
        print(f"{rank}. [Score: {score:.4f}] {text}")

if __name__ == "__main__":
    main()
