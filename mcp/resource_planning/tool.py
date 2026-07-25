"""
Resource Planning MCP Tool

Provides HR and workforce information to the StratOS AI Core.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"


def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def execute(query: str):
    hr_data = load_data()

    return {
        "tool": "resource_planning",
        "status": "success",
        "data": {
            "total_employees": hr_data["total_employees"],
            "engineering_team": hr_data["engineering_team"],
            "available_engineers": hr_data["available_engineers"],
            "open_positions": hr_data["open_positions"],
            "average_utilization": hr_data["average_utilization"],
            "average_salary": hr_data["average_salary"],
            "attrition_rate": hr_data["attrition_rate"],
            "hiring_budget": hr_data["hiring_budget"]
        }
    }


if __name__ == "__main__":
    print(execute("Can we hire 10 more engineers?"))