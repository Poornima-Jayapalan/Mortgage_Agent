from pathlib import Path

MODEL = "llama3.1:8b"
BASE_DIR = Path(__file__).resolve().parent.parent
VECTORSTORE_DIR = BASE_DIR / "vectorstores"
