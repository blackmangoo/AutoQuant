from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, Any
from app.agent import run_agent
import os

app = FastAPI(
    title="AutoQuant Financial Agent API",
    description="Multi-Agent system for financial analysis based on SEC filings and live market data.",
    version="0.1.0"
)

class AnalysisRequest(BaseModel):
    ticker: str
    lookback_days: int = 14

os.makedirs("app/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("app/static/index.html", "r") as f:
        return f.read()

@app.post("/analyze")
def trigger_analysis(req: AnalysisRequest) -> Dict[str, Any]:
    # Run the LangGraph Multi-Agent workflow
    result_state = run_agent(ticker=req.ticker, lookback=req.lookback_days)
    
    return {
        "ticker": req.ticker,
        "status": "success",
        "financial_data_summary": result_state.get("raw_financial_data", ""),
        "agent_analysis": result_state.get("final_analysis", "")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
