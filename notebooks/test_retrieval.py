"""
Test retrieval from Chroma vectorstore.
Make sure you have already built your vectorstore in /vectorstore.
"""

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

vectorstore = Chroma(
    persist_directory="vectorstore",
    embedding_function=FastEmbedEmbeddings()
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

query = "What is the interest rate?"
docs = retriever.get_relevant_documents(query)

print("\n=== Retrieval Results ===\n")
for i, d in enumerate(docs):
    print(f"--- Chunk {i+1} ---")
    print(d.page_content[:500])
    print()
