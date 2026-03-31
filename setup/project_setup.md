markdown
##  System Requirements

- **Python 3.10+** (recommended)
- **Ollama CLI** — required if running Llama 3.1 locally
- **Tesseract OCR** — required for scanned PDFs

### Install Tesseract OCR

brew install tesseract
Linux

bash
sudo apt install tesseract-ocr
Windows  
Download installer: https://github.com/UB-Mannheim/tesseract/wiki (github.com in Bing)

## Download the Required Model
bash
ollama pull llama3.1:8b
Optional smaller model (faster, less accurate)
bash
ollama pull mistral
Test the model
bash
ollama run llama3.1:8b
Type something like:

Code
Hello, how are you
Press Ctrl + D to exit.

##  Python Environment Setup
Create Python virtual environment
bash
python3 -m venv venv
Activate the environment
macOS / Linux

bash
source venv/bin/activate
Windows

bash
venv\Scripts\activate
Install dependencies
bash
pip install -r requirements.txt

## Verify Installation

Run this in Python to confirm everything is installed correctly:

python
try:
    import streamlit
    print("Streamlit installed ")
except ImportError:
    print("Streamlit NOT installed")

try:
    import langchain
    print("LangChain installed ")
except ImportError:
    print("LangChain NOT installed ")

try:
    import chromadb
    print("ChromaDB installed ")
except ImportError:
    print("ChromaDB NOT installed ")

try:
    import PyPDF2  # or pypdf depending on your version
    print("PyPDF installed ")
except ImportError:
    print("PyPDF NOT installed ")

try:
    import pytesseract
    print("Tesseract OCR installed ")
except ImportError:
    print("Tesseract OCR NOT installed ")
