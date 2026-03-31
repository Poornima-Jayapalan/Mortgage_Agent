#  Mortgage AI Agent (RAG + Tool-Using LLM)

## Project Overview

Build a **production-ready AI system** that analyzes real-world mortgage documents, answers complex financial questions, and performs dynamic reasoning using Retrieval-Augmented Generation (RAG) and tool-augmented LLM agents — all running locally.

This project demonstrates how to design and deploy **practical LLM systems** for document intelligence and financial analysis.

---

## Why This Project?

* Moves beyond basic chatbots into **tool-using AI systems**
* Combines **RAG + Agents + OCR** for real-world document handling
* Demonstrates **end-to-end LLM system design**
* Runs fully **local and cost-free** (no API dependency)
* Handles **messy real-world data** (PDFs, scanned docs)
* Showcases **production-relevant architecture patterns**

---

## 🛠️ Tech Stack (Local & Open Source)

### Core LLM

* Ollama — Run local LLMs (Llama 3.1)

### Frameworks

* LangChain — Agent orchestration and tool integration

### Vector Database

* ChromaDB — Embedding storage and retrieval

### Embeddings

* FastEmbed — Lightweight, fast embedding generation

### Document Processing

* PyPDFLoader — PDF parsing
* Tesseract OCR — Scanned document handling

### Tools

* DuckDuckGo Search — Real-time mortgage rate lookup
* Custom Calculator Tool — Financial computations

### UI

* Streamlit — Interactive chat interface

---

## System Architecture

```
User (Streamlit UI)
        ↓
Document Upload (Mortgage PDF)
        ↓
Text Extraction
   ├── PyPDF (digital)
   └── OCR (scanned docs)
        ↓
Text Chunking (Recursive Splitter)
        ↓
Embeddings (FastEmbed)
        ↓
Vector Store (ChromaDB)
        ↓
Retriever (Top-K Semantic Search)
        ↓
LangChain Agent
   ├── Document Search Tool
   ├── Calculator Tool
   └── Web Search Tool
        ↓
Local LLM (Ollama - Llama 3.1)
        ↓
Final Answer
```

---

##  Key System Capabilities

### 1. Document Intelligence (RAG)

* Converts mortgage PDFs into searchable embeddings
* Retrieves only relevant clauses for grounded answers
* Reduces hallucinations via context injection

### 2. Tool-Augmented Reasoning

The agent dynamically decides when to:

* Query the document
* Perform financial calculations
* Fetch live market data

### 3. OCR for Real-World Robustness

* Automatically detects low-text PDFs
* Falls back to OCR for scanned/image-based documents

### 4. Interactive AI Interface

* Chat-based UX built with Streamlit
* Maintains session history
* Real-time responses

---

## Implementation Breakdown

### Phase 1: Document Ingestion & RAG

* Load and parse mortgage PDFs
* Implement chunking strategy
* Generate embeddings with FastEmbed
* Store vectors in ChromaDB
* Build retriever for semantic search

### Phase 2: Agent System

* Define tools:

  * Document search
  * Calculator (safe eval)
  * Web search
* Initialize LangChain agent (zero-shot reasoning)
* Enable tool selection via natural language queries

### Phase 3: UI & Interaction

* Build Streamlit chat interface
* Add session memory
* Display responses in conversational format

### Phase 4: Robustness Enhancements

* OCR fallback for scanned PDFs
* Error handling for tool execution
* Caching for performance optimization

---

##  Example Use Cases

* Extract interest rates and loan terms
* Compare mortgage against current market rates
* Calculate alternative payment scenarios
* Estimate total interest over loan lifetime
* Analyze clauses from lengthy contracts

---

## Why This Project Matters

Most LLM projects:

* Stop at simple chat interfaces
* Lack grounding in real data
* Ignore real-world input complexity

This project demonstrates:

* **Grounded AI (RAG)** for accuracy
* **Agent-based reasoning** for flexibility
* **Tool integration** for real-world usefulness
* **Local deployment** for privacy and cost control
* **Robust data handling** (including OCR edge cases)

This reflects how modern **production AI systems are actually built**.

---

## Potential Enhancements

* Multi-document comparison (e.g., multiple loans)
* Source citation highlighting
* Financial analytics dashboard
* Migration to LangGraph for advanced agent workflows
* Cloud deployment (AWS / Docker / Streamlit Cloud)
* Evaluation pipeline (RAG accuracy, hallucination detection)

---

## Success Metrics

* **Answer Accuracy** — Correctness of financial/document answers
* **Retrieval Quality** — Relevance of returned document chunks
* **Latency** — Response time per query
* **Tool Usage Efficiency** — Correct tool selection by agent
* **Robustness** — Performance on scanned vs clean PDFs
