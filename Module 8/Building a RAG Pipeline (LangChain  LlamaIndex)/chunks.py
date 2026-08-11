import json
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_chunk(file_path: str) -> list[str]:
    """Load a text file and split it into overlapping chunks."""

    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    print(f"Loaded {len(raw_text)} characters from {file_path}")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = text_splitter.split_text(raw_text)

    print(f"Split into {len(chunks)} chunks")

    return chunks


def save_chunks(chunks: list[str], output_file: str) -> None:
    """Save chunks to a JSON file."""

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"Chunks saved to {output_file}")


if __name__ == "__main__":
    chunks = load_and_chunk("KB.txt")
    save_chunks(chunks, "chunks.json")