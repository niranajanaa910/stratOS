from fastapi import APIRouter

from schemas.api import StrategyRequest, StrategyResponse

from registry.tool_registry import ToolRegistry
from agent.orchestrator import Orchestrator

router = APIRouter()

# Create registry
registry = ToolRegistry()

# Create orchestrator
orchestrator = Orchestrator(registry)


@router.post("/strategy", response_model=StrategyResponse)
def generate_strategy(request: StrategyRequest):

    result = orchestrator.execute(request.prompt)

    return StrategyResponse(result=result)
