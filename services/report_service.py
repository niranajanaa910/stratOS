from schemas.reasoning import ReasoningResponse


class ReportService:
    """
    Formats the final strategy result into a clean report.
    """

    def generate_report(self, result: ReasoningResponse) -> dict:

        return {
            "decision": result.decision,
            "confidence": result.confidence,
            "reasons": result.reason,
            "recommended_actions": result.actions
        }