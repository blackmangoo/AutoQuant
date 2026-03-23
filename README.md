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
    A[Premium Bloomberg UI Dashboard] -->|User Inputs Ticker| B(FastAPI Endpoint: POST /analyze)
    B -->|State Trigger| C(LangGraph: Fetch Node)
    C -->|yfinance Data Streams| D{(Market Fundamentals State)}
    D --> E(LangGraph: Analyst Node)
    E -->|Gemini 1.5 Flash Reasoning| F[Multi-Agent Synergy Output]
    F -->|JSON Response| G[Dashboard Terminal Display]
```

## 🧠 Core Features
1. **Multi-Agent Orchestration**: Replaces standard prompts with an autonomous LangGraph lifecycle mimicking a real quantitative analyst pipeline.
2. **Bloomberg-Style Dark UI**: An immersive, localized dashboard mapping agentic states directly onto a real-time terminal UI.
3. **Data-Driven Analysis**: Leverages direct Python `yfinance` pipelines so the LLM calculates decisions strictly on live numbers.

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
