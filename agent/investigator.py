from typing import List

from schemas.mcp import MCPResponse


class Investigator:
    """
    Calls the required MCP tools and collects evidence.
    """

    def __init__(self, registry):
        self.registry = registry

    def investigate(self, required_tools: List[str]) -> List[MCPResponse]:

        evidence = []

        for tool_name in required_tools:

            tool = self.registry.get_tool(tool_name)

            if tool is None:
                continue

            try:
                result = tool.execute()

                evidence.append(result)

            except Exception as e:

                evidence.append(
                    MCPResponse(
                        tool=tool_name,
                        status="failure",
                        data={
                            "error": str(e)
                        }
                    )
                )

        return evidence