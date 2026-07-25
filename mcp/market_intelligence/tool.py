from .server import MarketIntelligenceServer


class MarketIntelligenceTool:
    """
    Wrapper class that exposes the Market Intelligence MCP
    to the StratOS Tool Registry.
    """

    def __init__(self):
        self.server = MarketIntelligenceServer()

    def execute(self, query: str):
        return self.server.execute(query)


# Local testing
if __name__ == "__main__":
    tool = MarketIntelligenceTool()

    result = tool.execute(
        "Should we expand into Germany?"
    )

    print(result)