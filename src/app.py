import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from src.loader import load_document
from src.agent import build_agent

st.set_page_config(page_title="Mortgage AI Agent", layout="wide")
st.title("🏠 Mortgage AI Agent")

st.caption("Upload a mortgage PDF and ask questions about it.")

# Sidebar
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

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Main
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
