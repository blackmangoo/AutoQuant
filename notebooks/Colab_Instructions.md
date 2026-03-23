# AutoQuant: Colab Sandbox

To experiment with our LangGraph Multi-Agent financial loop before baking it into the FastAPI production backend, you can use Google Colab.

### 1. Setup Environment
In a new Colab cell, install the required libraries:
```python
!pip install -q langgraph langchain langchain-openai yfinance python-dotenv
```

### 2. Configure API Key
```python
import os
import getpass

# Provide your key securely
os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API Key: ")
```

### 3. Agentic Loop (Draft)
You can experiment with `yfinance` to fetch live data (e.g., `NVDA`, `AAPL`) and pass it to a LangGraph `StateGraph` that acts as the fundamental analyst and the risk manager.
Once the prompts are tuned, we will copy that exact logic into the local `app/main.py` FastAPI route!
