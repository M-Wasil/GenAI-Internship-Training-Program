import os
from dotenv import load_dotenv
from openai import OpenAI

from retrieve import retrieve


# Step 1: Load environment variables

load_dotenv()


# Step 2: Set up OpenRouter client

client = OpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)


# Step 3: Build a prompt using retrieved context

def build_prompt(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""Answer the question using ONLY the context below.
If the answer isn't in the context, say you don't know.

Context:
{context}

Question: {query}

Answer:"""

    return prompt


# Step 4: Retrieve context and generate an answer

def generate_answer(query):
    results = retrieve(query, top_k=3)

    context_chunks = [doc.page_content for doc in results]

    prompt = build_prompt(query, context_chunks)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


# Step 5: Test the RAG pipeline

if __name__ == "__main__":
    query = "Where are Aurora Peak tents manufactured?"

    answer = generate_answer(query)

    print(f"\nQuestion: {query}\n")
    print(f"Answer: {answer}")

