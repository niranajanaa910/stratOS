import json
from pathlib import Path


class ComplianceServer:
    """
    MCP Server for Compliance.
    Reads compliance information and returns it
    in the standard StratOS MCP format.
    """

    def __init__(self):
        self.data_file = Path(__file__).parent / "data.json"

    def execute(self, query: str):

        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            return {
                "tool": "compliance",
                "status": "success",
                "data": data
            }

        except Exception as e:
            return {
                "tool": "compliance",
                "status": "error",
                "data": {
                    "message": str(e)
                }
            }


if __name__ == "__main__":
    server = ComplianceServer()
    print(server.execute("Check compliance"))