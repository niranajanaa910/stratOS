from typing import Callable, Dict, List


class ToolRegistry:
    """
    Stores all available MCP tools.
    """

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, name: str, tool: Callable):
        """
        Register an MCP tool.
        """
        self._tools[name] = tool

    def get_tool(self, name: str):
        """
        Retrieve a registered MCP.
        """
        return self._tools.get(name)

    def list_tools(self) -> List[str]:
        """
        Return names of all registered MCPs.
        """
        return list(self._tools.keys())