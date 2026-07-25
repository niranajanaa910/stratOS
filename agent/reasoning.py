from typing import List

from schemas.mcp import MCPResponse
from schemas.reasoning import ReasoningResponse


class ReasoningEngine:
    """
    Generates the final business decision based on MCP evidence.
    """

    def reason(self, evidence: List[MCPResponse]) -> ReasoningResponse:

        reasons = []

        actions = []

        confidence = 50

        decision = "REVIEW"

        successful_tools = 0

        for result in evidence:

            if result.status == "success":

                successful_tools += 1

                reasons.append(
                    f"{result.tool} analysis completed successfully."
                )

            else:

                reasons.append(
                    f"{result.tool} could not provide data."
                )

        if successful_tools >= 3:

            decision = "GO"

            confidence = 90

            actions = [
                "Proceed with implementation.",
                "Notify stakeholders.",
                "Prepare execution plan."
            ]

        elif successful_tools >= 1:

            decision = "REVIEW"

            confidence = 70

            actions = [
                "Collect additional information.",
                "Review business risks."
            ]

        else:

            decision = "NO GO"

            confidence = 30

            actions = [
                "Do not proceed.",
                "Re-evaluate business strategy."
            ]

        return ReasoningResponse(
            decision=decision,
            confidence=confidence,
            reason=reasons,
            actions=actions
        )