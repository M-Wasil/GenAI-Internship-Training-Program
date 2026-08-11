import json
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_chunks(file_path: str) -> list[str]:
    """Load text chunks from a JSON file."""

    with open(file_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"Loaded {len(chunks)} chunks from {file_path}")

    return chunks


def create_faiss_index(chunks: list[str], index_path: str) -> None:
    """Create and save a FAISS index from text chunks."""

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS index...")

    vector_store = FAISS.from_texts(
        chunks,
        embedding=embeddings
    )

    vector_store.save_local(index_path)

    print(f"FAISS index saved to {index_path}")


if __name__ == "__main__":
    chunks = load_chunks("chunks.json")
    create_faiss_index(chunks, "faiss_index")