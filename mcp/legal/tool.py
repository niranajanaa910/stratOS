from .server import LegalServer


class LegalTool:

    def __init__(self):
        self.server = LegalServer()

    def execute(self, query: str):
        return self.server.execute(query)