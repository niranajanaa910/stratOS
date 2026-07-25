from pydantic import BaseModel, Field
from typing import List


class PlannerRequest(BaseModel):
    """
    Request received from the frontend.
    """
    prompt: str = Field(..., description="Business question from the user")


class PlannerResponse(BaseModel):
    """
    Output produced by the Planner.
    """
    goal: str = Field(..., description="Identified business objective")
    required_tools: List[str] = Field(
        ...,
        description="List of MCP tools required to answer the prompt"
    )