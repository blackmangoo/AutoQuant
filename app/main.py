from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from app.agent import run_agent

app = FastAPI(
    title="AutoQuant Financial Agent API",
    description="Multi-Agent system for financial analysis based on SEC filings and live market data.",
    version="0.1.0"
)

class AnalysisRequest(BaseModel):
    ticker: str
    lookback_days: int = 14

@app.get("/")
def read_root():
    return {"status": "AutoQuant Engine Running inside FastAPI"}

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
