from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="AutoQuant Financial Agent API",
    description="Multi-Agent system for financial analysis based on SEC filings and live market data.",
    version="0.1.0"
)

class AnalysisRequest(BaseModel):
    ticker: str
    lookback_days: int = 30

@app.get("/")
def read_root():
    return {"status": "AutoQuant Engine Running inside FastAPI"}

@app.post("/analyze")
def trigger_analysis(req: AnalysisRequest) -> Dict[str, Any]:
    # TODO: Integrate LangGraph multi-agent workflow here
    # 1. Fetch live market info via yfinance
    # 2. Trigger risk analyst and fundamentals analyst agents
    # 3. Compile output
    
    return {
        "ticker": req.ticker,
        "status": "success",
        "message": "Agentic loop triggered (Mocked).",
        "mock_signals": {
            "trend": "BULLISH",
            "confidence": 0.85
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
