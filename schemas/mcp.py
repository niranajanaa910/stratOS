from pydantic import BaseModel, Field
from typing import Dict, Any


class MCPResponse(BaseModel):
    """
    Standard response returned by every MCP tool.
    """
    tool: str = Field(..., description="Name of the MCP tool")
    status: str = Field(..., description="success or failure")
    data: Dict[str, Any] = Field(
        default_factory=dict,
        description="Tool-specific data returned by the MCP"
    )