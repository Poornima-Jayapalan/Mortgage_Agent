## Mortgage AI Agent (RAG + Tool‑Using LLM)
## Project Overview
Mortgage AI Agent is an AI-powered tool that combines RAG (Retrieval-Augmented Generation) with tool-using LLMs to intelligently process mortgage documents. 
## Why this Project
- **Grounding AI with RAG:** Ensures answers come from actual mortgage documents rather than hallucinated text.
- **Agent-based reasoning:** Dynamically chooses when to search documents, calculate, or fetch live data.
- **Tool integration for real-world usefulness:** Combines web search, financial calculators, and PDF/OCR handling.
- **Robust document handling:** Works with both digital PDFs and scanned/image-based documents.
- **Local deployment:** Maintains privacy and reduces cloud costs.
## Tech Stack (100% Free & Open Source)
## Vector Database
- **ChromaDB** — Embedding storage and retrieval

## Embeddings
- **FastEmbed** — Lightweight, fast embedding generation

## Document Processing
- **PyPDFLoader** — PDF parsing
- **Tesseract OCR** — Scanned document handling

## Tools
- **DuckDuckGo Search** — Real-time mortgage rate lookup
- **Custom Calculator Tool** — Financial computations

## UI
- **Streamlit** — Interactive chat interface

## Key System Capabilities

1. **Document Intelligence (RAG)**
   - Converts mortgage PDFs into searchable embeddings
   - Retrieves only relevant clauses for grounded answers
   - Reduces hallucinations via context injection

2. **Tool‑Augmented Reasoning**
   - Dynamically decides when to:
     - Query the document
     - Perform financial calculations
     - Fetch live market data

3. **OCR for Real‑World Robustness**
   - Automatically detects low‑text PDFs
   - Falls back to OCR for scanned/image-based documents

4. **Interactive AI Interface**
   - Chat-based UX built with Streamlit
   - Maintains session history
   - Real-time responses

---


## Implementation Breakdown

**Phase 1: Document Ingestion & RAG**

Load and parse mortgage PDFs
Implement chunking strategy
Generate embeddings with FastEmbed
Store vectors in ChromaDB
Build retriever for semantic search

**Phase 2: Agent System**

Define tools:
Document search
Calculator (safe eval)
Web search
Initialize LangChain agent (zero-shot reasoning):
Enable tool selection via natural language queries

**Phase 3: UI & Interaction**

Build Streamlit chat interface
Add session memory
Display responses in conversational format

**Phase 4: Robustness Enhancements**

OCR fallback for scanned PDFs
Error handling for tool execution
Caching for performance optimization
 Example Use Cases
Extract interest rates and loan terms
Compare mortgage against current market rates
Calculate alternative payment scenarios
Estimate total interest over loan lifetime
Analyze clauses from lengthy contracts

## Success Metrics
**Answer Accuracy** — Correctness of financial/document answers

**Retrieval Quality** — Relevance of returned document chunks

**Latency** — Response time per query

**Tool Usage Efficiency** — Correct tool selection by agent

**Robustness** — Performance on scanned vs clean PDFs


