"""
Financial Analysis MCP Tool

This module provides financial information to the StratOS AI Core.

It DOES NOT make decisions.
It ONLY returns financial evidence.
"""

import json
from pathlib import Path


# Path to this folder's data.json
DATA_FILE = Path(__file__).parent / "data.json"


def load_data():
    """
    Load financial data from data.json
    """

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def execute(query: str):
    """
    Standard MCP Entry Point

    Parameters
    ----------
    query : str
        User's business question

    Returns
    -------
    dict
        Standard StratOS MCP response
    """

    financial_data = load_data()

    return {
        "tool": "financial_analysis",
        "status": "success",
        "data": {
            "budget": financial_data["budget"],
            "cash_reserves": financial_data["cash_reserves"],
            "annual_revenue": financial_data["annual_revenue"],
            "annual_profit": financial_data["annual_profit"],
            "profit_margin": financial_data["profit_margin"],
            "operating_cost": financial_data["operating_cost"],
            "roi": financial_data["roi"],
            "debt_ratio": financial_data["debt_ratio"],
            "available_investment": financial_data["available_investment"]
        }
    }
    
    
    
    
if __name__ == "__main__":
    result = execute("Should we increase Product X price?")
    print(result)
        
        