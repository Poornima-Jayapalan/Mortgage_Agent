import tempfile
import os
import hashlib
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .ocr import extract_with_ocr
from .config import VECTORSTORE_DIR


def stable_hash(filename: str) -> str:
    return hashlib.md5(filename.encode()).hexdigest()[:10]


def load_document(file_bytes, filename):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(file_bytes)
        tmp_path = f.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()

    total_text = " ".join(p.page_content for p in pages).strip()

    if len(total_text) < 100:
        pages = extract_with_ocr(tmp_path)

    os.unlink(tmp_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(pages)

    embeddings = FastEmbedEmbeddings()

    persist_dir = str(VECTORSTORE_DIR / f"vectorstore_{stable_hash(filename)}")

    vectorstore = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=persist_dir
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    return retriever, pages, len(pages)
