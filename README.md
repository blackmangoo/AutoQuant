<div align="center">
  <h1>📈 AutoQuant</h1>
  <p><b>Autonomous Multi-Agent Hedge Fund Analyst</b></p>
  
  [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
  [![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-FF9900.svg)](https://python.langchain.com/docs/langgraph)
  [![Gemini 1.5](https://img.shields.io/badge/LLM-Gemini_1.5_Flash-8E75B2.svg)](https://deepmind.google/technologies/gemini/)
</div>

---

## 🚀 Overview
**AutoQuant** is an advanced, domain-specific AI system designed for the financial sector. Moving beyond simple single-shot LLM prompts, AutoQuant orchestrates a **Multi-Agent workflow** (powered by LangGraph and Gemini 1.5 Flash) to retrieve real-time market data, aggregate financial fundamentals, and synthesize quantitative buying/selling signals.

## 🏗️ Architecture
```mermaid
graph TD
    A[FastAPI Endpoint: POST /analyze] -->|Ticker & Lookback| B(StateGraph: Fetch Node)
    B -->|yfinance API Calls| C{(Raw Financial Data State)}
    C --> D(StateGraph: Analyst Node)
    D -->|LangChain + Gemini 1.5| E[Final Buy/Sell/Hold Signal]
    E --> F[API JSON Response]
```

## 🧠 How it Works
1. **Request Trigger:** A REST POST call is made to the FastAPI backend containing a stock ticker.
2. **Fetch Node:** The LangGraph execution flow triggers the Data Fetcher, pulling historical pricing, moving averages, and sector info via `yfinance`.
3. **Analyst Node:** The raw financial state is passed into a highly specialized Gemini 1.5 System Prompt acting as a Senior Quantitative Analyst. 
4. **Synthesis:** The LLM evaluates the context window strictly against financial principles to output an optimized trading thesis.

## 🛠️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/blackmangoo/AutoQuant.git
cd AutoQuant
```

### 2. Environment Setup
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. API Keys
Rename `.env.example` to `.env` and insert your Gemini API key:
```env
GEMINI_API_KEY=your_key_here
```

### 4. Run the API Engine
```bash
uvicorn app.main:app --reload
```
Visit `http://localhost:8000/docs` to test the `/analyze` endpoint!
