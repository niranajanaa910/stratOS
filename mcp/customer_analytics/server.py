import json
from pathlib import Path


class CustomerAnalyticsServer:
    """
    MCP Server for Customer Analytics.
    Reads customer insights and returns them
    in the standard StratOS MCP format.
    """

    def __init__(self):
        self.data_file = Path(__file__).parent / "data.json"

    def execute(self, query: str) -> dict:
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            return {
                "tool": "customer_analytics",
                "status": "success",
                "data": data
            }

        except Exception as e:
            return {
                "tool": "customer_analytics",
                "status": "error",
                "data": {
                    "message": str(e)
                }
            }


if __name__ == "__main__":
    server = CustomerAnalyticsServer()

    result = server.execute(
        "Should we increase product price?"
    )

    print(json.dumps(result, indent=4))