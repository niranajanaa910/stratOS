from schemas.planner import PlannerRequest, PlannerResponse


class Planner:
    """
    Identifies the business goal and selects the MCP tools
    required to answer the user's prompt.
    """

    def __init__(self, registry):
        self.registry = registry

    def plan(self, request: PlannerRequest) -> PlannerResponse:

        prompt = request.prompt.lower()

        # Market Expansion
        if "expand" in prompt or "country" in prompt or "market" in prompt:
            return PlannerResponse(
                goal="Market Expansion",
                required_tools=[
                    "financial_analysis",
                    "market_intelligence",
                    "resource_planning",
                    "legal"
                ]
            )

        # Hiring
        elif "hire" in prompt or "recruit" in prompt:
            return PlannerResponse(
                goal="Hiring Decision",
                required_tools=[
                    "financial_analysis",
                    "resource_planning"
                ]
            )

        # Pricing
        elif "price" in prompt or "pricing" in prompt:
            return PlannerResponse(
                goal="Pricing Strategy",
                required_tools=[
                    "financial_analysis",
                    "customer_analytics",
                    "market_intelligence"
                ]
            )

        # Default
        return PlannerResponse(
            goal="General Business Strategy",
            required_tools=self.registry.list_tools()
        )