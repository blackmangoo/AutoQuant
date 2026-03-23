🚀 **Excited to open-source my latest AI project: AutoQuant!** 📈

As a 7th-semester BS AI student at FAST-NU, I've noticed many AI projects stop at basic RAG or single-shot prompting. I wanted to push the boundaries of what's possible in **FinTech** by engineering a fully autonomous **Multi-Agent workflow**. 

Meet **AutoQuant** — an AI-powered Quantitative Analyst built directly into a high-performance REST API. 

Instead of relying on a single LLM call, AutoQuant leverages **LangGraph** to coordinate a deterministic state machine:
1️⃣ **Data Fetcher Node:** Hooks into live market feeds (`yfinance`) to assemble a real-time state vector of pricing and sector fundamentals.
2️⃣ **Analyst Agent (Gemini 1.5 Flash):** Ingests the data using specialized system prompts to synthesize a concrete Buy/Sell/Hold thesis.

🛠️ **Tech Stack:**
- **Agentic Orchestration:** LangGraph, LangChain
- **LLM Engine:** Google Gemini 1.5 Flash
- **Backend Architecture:** FastAPI, Pydantic, Uvicorn (Asynchronous API)
- **Financial Pipelines:** yfinance

Building this taught me exactly how to transition ML models from flat Jupyter Notebooks into dynamic, stateful enterprise backend systems. 

Check out the code and architecture here: https://github.com/blackmangoo/AutoQuant

#ArtificialIntelligence #MachineLearning #LangGraph #FastAPI #FinTech #QuantitativeAnalysis #FASTNU #AIResearch #SoftwareEngineering
