from fastapi import FastAPI
from tool import analyze_market

app = FastAPI(title="Market Intelligence MCP")


@app.get("/")
def home():
    return {
        "service": "Market Intelligence MCP",
        "status": "Running"
    }


@app.post("/analyze")
def analyze(request: dict):
    goal = request.get("goal", "")
    return analyze_market(goal)