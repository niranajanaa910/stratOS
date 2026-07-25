import json
from pathlib import Path


class MarketIntelligenceServer:
    """
    MCP Server for Market Intelligence.
    Reads mock enterprise market data and returns it in the standard StratOS format.
    """

    def __init__(self):
        self.data_file = Path(__file__).parent / "data.json"

    def execute(self, query: str) -> dict:
        """
        Executes a Market Intelligence query.

        Args:
            query (str): User's strategic question.

        Returns:
            dict: Standard MCP response.
        """

        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            return {
                "tool": "market_intelligence",
                "status": "success",
                "data": data
            }

        except Exception as e:
            return {
                "tool": "market_intelligence",
                "status": "error",
                "data": {
                    "message": str(e)
                }
            }


# Local testing
if __name__ == "__main__":
    server = MarketIntelligenceServer()

    response = server.execute(
        "Should we expand into Germany?"
    )

    print(json.dumps(response, indent=4))