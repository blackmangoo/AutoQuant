import os
import yfinance as yf
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

# Define the state for the LangGraph agent
class AgentState(TypedDict):
    ticker: str
    lookback_days: int
    raw_financial_data: str
    final_analysis: str

# 1. Fetch Node
def fetch_financial_data(state: AgentState):
    ticker_sym = state["ticker"]
    stock = yf.Ticker(ticker_sym)
    
    # Extract simple summary of historical financial data
    try:
        hist = stock.history(period=f"{state['lookback_days']}d")
        close_prices = hist['Close'].tolist()
        info = stock.info
        
        data_summary = f"Company: {info.get('longName', ticker_sym)}\n"
        data_summary += f"Sector: {info.get('sector', 'N/A')}\n"
        data_summary += f"Recent {state['lookback_days']}-day close prices: {[round(p, 2) for p in close_prices]}\n"
    except Exception as e:
        data_summary = f"Error fetching data for {ticker_sym}: {str(e)}"
        
    return {"raw_financial_data": data_summary}

# 2. Analyze Node (Powered by Gemini model)
def compute_analysis(state: AgentState):
    # Retrieve Gemini API Key from environment mapped during .env load
    if not os.getenv("GEMINI_API_KEY") and not os.getenv("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = os.getenv("OPENAI_API_KEY", "") # Fallback mapping if user misused OPENAI key slot
    elif os.getenv("GEMINI_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
    
    sys_msg = SystemMessage(content="You are AutoQuant, an expert AI hedge fund analyst. Analyze the raw data and output a concise buy/sell/hold signal with a brief justification.")
    user_msg = HumanMessage(content=f"Here is the data for {state['ticker']}:\n{state['raw_financial_data']}")
    
    try:
        response = llm.invoke([sys_msg, user_msg])
        analysis = response.content
    except Exception as e:
        analysis = f"Error invoking Gemini API: {str(e)}"
        
    return {"final_analysis": analysis}

# Build the execution Graph
workflow = StateGraph(AgentState)

# Register nodes
workflow.add_node("fetcher", fetch_financial_data)
workflow.add_node("analyst", compute_analysis)

# Define exact execution edges
workflow.set_entry_point("fetcher")
workflow.add_edge("fetcher", "analyst")
workflow.add_edge("analyst", END)

# Compile into an executable application
app_graph = workflow.compile()

def run_agent(ticker: str, lookback: int = 30):
    initial_state = {
        "ticker": ticker,
        "lookback_days": lookback,
        "raw_financial_data": "",
        "final_analysis": ""
    }
    
    # Trigger graph execution
    final_state = app_graph.invoke(initial_state)
    return final_state
