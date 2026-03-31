import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import tempfile
import os
import hashlib
from pathlib import Path

# LangChain
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from langchain.agents import initialize_agent, AgentType

MODEL = "llama3.1:8b"
SCRIPT_DIR = Path(__file__).parent


def stable_hash(filename: str) -> str:
    return hashlib.md5(filename.encode()).hexdigest()[:10]


@st.cache_resource
def get_model():
    return ChatOllama(model=MODEL, temperature=0)


def extract_with_ocr(tmp_path):
    try:
        import pytesseract
        from pdf2image import convert_from_path
        from langchain_core.documents import Document

        images = convert_from_path(tmp_path)
        pages = []

        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            pages.append(Document(page_content=text, metadata={"page": i}))

        return pages

    except ImportError:
        st.warning("Install OCR deps: pip install pytesseract pdf2image Pillow")
        return []


@st.cache_resource(show_spinner="Indexing document...")
def load_document(file_bytes, filename):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(file_bytes)
        tmp_path = f.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()

    total_text = " ".join(p.page_content for p in pages).strip()

    if len(total_text) < 100:
        st.info("Scanned PDF detected — running OCR...")
        pages = extract_with_ocr(tmp_path)

    os.unlink(tmp_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(pages)

    embeddings = FastEmbedEmbeddings()

    persist_dir = str(SCRIPT_DIR / f"vectorstore_{stable_hash(filename)}")

    vectorstore = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=persist_dir
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    return retriever, pages, len(pages)


def build_agent(retriever):
    model = get_model()

    @tool
    def search_mortgage_doc(query: str) -> str:
        """Search the uploaded mortgage document."""
        docs = retriever.invoke(query)
        return "\n\n".join(d.page_content for d in docs)

    @tool
    def calculate(expression: str) -> str:
        """Perform math calculations."""
        try:
            return str(eval(expression, {"__builtins__": {}}))
        except Exception as e:
            return f"Error: {e}"

    @tool
    def web_search(query: str) -> str:
        """Search current mortgage rates."""
        return DuckDuckGoSearchRun().run(query)

    tools = [search_mortgage_doc, calculate, web_search]

    agent = initialize_agent(
        tools=tools,
        llm=model,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent


st.set_page_config(page_title="Mortgage AI Agent", layout="wide")
st.title("🏠 Mortgage AI Agent")
st.caption("Upload a mortgage PDF and ask questions about it.")

with st.sidebar:
    st.header("Upload Document")
    uploaded_file = st.file_uploader("Choose a mortgage PDF", type="pdf")

    st.divider()
    st.markdown("### Try asking:")
    st.markdown("- What is my interest rate?")
    st.markdown("- Compare my rate to market rates")
    st.markdown("- What would my payment be at 6%?")
    st.markdown("- Total interest paid?")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if uploaded_file:
    retriever, pages, page_count = load_document(
        uploaded_file.getvalue(),
        uploaded_file.name
    )

    st.success(f"Loaded: {uploaded_file.name} ({page_count} pages)")

    agent = build_agent(retriever)

    question = st.chat_input("Ask about your mortgage...")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    result = agent.run(question)
                except Exception as e:
                    result = f"Error: {str(e)}"

                st.markdown(result)

        st.session_state.messages.append({"role": "assistant", "content": result})

else:
    st.info("Upload a mortgage PDF to get started.")

    st.markdown("""
    ### How this agent works

    1. Reads your uploaded mortgage document  
    2. Searches relevant clauses  
    3. Optionally checks market rates  
    4. Runs calculations  
    5. Returns a clear answer  

    The agent decides which tools to use automatically.
    """)
