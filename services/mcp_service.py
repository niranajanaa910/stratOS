from typing import List

from schemas.mcp import MCPResponse


class MCPService:
    """
    Handles communication with registered MCP tools.
    """

    def __init__(self, registry):
        self.registry = registry

    def execute_tools(self, required_tools: List[str]) -> List[MCPResponse]:

        responses = []

        for tool_name in required_tools:

            tool = self.registry.get_tool(tool_name)

            if tool is None:
                continue

            try:
                response = tool.execute()

                responses.append(response)

            except Exception as e:

                responses.append(
                    MCPResponse(
                        tool=tool_name,
                        status="failure",
                        data={
                            "error": str(e)
                        }
                    )
                )

        return responses