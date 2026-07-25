import json
from pathlib import Path


class LegalServer:

    def __init__(self):
        self.data_file = Path(__file__).parent / "data.json"

    def execute(self, query: str):

        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            return {
                "tool": "legal",
                "status": "success",
                "data": data
            }

        except Exception as e:
            return {
                "tool": "legal",
                "status": "error",
                "data": {
                    "message": str(e)
                }
            }


if __name__ == "__main__":
    server = LegalServer()
    print(server.execute("Expand into Germany"))