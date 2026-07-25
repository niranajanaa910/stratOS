from schemas.planner import PlannerRequest
from schemas.reasoning import ReasoningResponse

from agent.planner import Planner
from agent.investigator import Investigator
from agent.reasoning import ReasoningEngine
from agent.actions import ActionGenerator


class Orchestrator:
    """
    Coordinates the complete strategy generation workflow.
    """

    def __init__(self, registry):

        self.planner = Planner(registry)
        self.investigator = Investigator(registry)
        self.reasoning = ReasoningEngine()
        self.action_generator = ActionGenerator()

    def execute(self, prompt: str) -> ReasoningResponse:

        # Step 1: Planning
        plan = self.planner.plan(
            PlannerRequest(prompt=prompt)
        )

        # Step 2: Investigation
        evidence = self.investigator.investigate(
            plan.required_tools
        )

        # Step 3: Reasoning
        result = self.reasoning.reason(evidence)

        # Step 4: Generate actions
        generated_actions = self.action_generator.generate(
            result.decision
        )

        # Replace default actions with structured actions
        result.actions = [
            action.title for action in generated_actions
        ]

        return result