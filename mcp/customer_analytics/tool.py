from .server import CustomerAnalyticsServer


class CustomerAnalyticsTool:
    """
    Wrapper for the Customer Analytics MCP.
    """

    def __init__(self):
        self.server = CustomerAnalyticsServer()

    def execute(self, query: str):
        return self.server.execute(query)


if __name__ == "__main__":
    tool = CustomerAnalyticsTool()
    print(tool.execute("Should we increase product price?"))