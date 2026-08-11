from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
FAISS_INDEX_PATH = "faiss_index"


def load_vector_store():
    """Load the saved FAISS vector store."""

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_store = FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def retrieve(query: str, top_k: int = 3):
    """Retrieve the most relevant chunks for a query."""

    vector_store = load_vector_store()

    results = vector_store.similarity_search(
        query,
        k=top_k
    )

    return results


if __name__ == "__main__":
    query = "Where are Aurora Peak tents manufactured?"

    results = retrieve(query)

    print(f"\nTop {len(results)} chunks for query: '{query}'\n")

    for i, doc in enumerate(results, 1):
        print(f"--- Result {i} ---")
        print(doc.page_content)
        print()