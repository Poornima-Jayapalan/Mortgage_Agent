"""
Test text chunking using RecursiveCharacterTextSplitter.
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path

text_file = Path("sample_docs/mortgage_text.txt")

if not text_file.exists():
    raise FileNotFoundError("Add a text file at sample_docs/mortgage_text.txt")

text = text_file.read_text()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=80
)

chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")
print("\n=== First Chunk ===\n")
print(chunks[0])
print("\n=== Second Chunk ===\n")
print(chunks[1])
