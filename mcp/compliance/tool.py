from .server import ComplianceServer


class ComplianceTool:

    def __init__(self):
        self.server = ComplianceServer()

    def execute(self, query: str):
        return self.server.execute(query)