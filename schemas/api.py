from pydantic import BaseModel, Field

from schemas.reasoning import ReasoningResponse


class StrategyRequest(BaseModel):
    """
    Request received from the frontend.
    """

    prompt: str = Field(
        ...,
        description="Business question"
    )


class StrategyResponse(BaseModel):
    """
    Response returned to the frontend.
    """

    result: ReasoningResponse