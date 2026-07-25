from pydantic import BaseModel, Field
from typing import Literal


class Action(BaseModel):
    """
    Represents a recommended business action.
    """

    title: str = Field(..., description="Action title")

    description: str = Field(
        ...,
        description="Detailed explanation of the action"
    )

    priority: Literal["High", "Medium", "Low"] = Field(
        default="Medium",
        description="Priority level"
    )