from typing import List

from schemas.action import Action


class ActionGenerator:
    """
    Converts AI decisions into structured business actions.
    """

    def generate(self, decision: str) -> List[Action]:

        actions = []

        if decision == "GO":

            actions.extend([
                Action(
                    title="Proceed with Strategy",
                    description="Begin executing the approved business strategy.",
                    priority="High"
                ),
                Action(
                    title="Notify Stakeholders",
                    description="Inform all relevant teams about the decision.",
                    priority="High"
                ),
                Action(
                    title="Prepare Execution Plan",
                    description="Create a detailed implementation roadmap.",
                    priority="Medium"
                )
            ])

        elif decision == "REVIEW":

            actions.extend([
                Action(
                    title="Collect More Data",
                    description="Gather additional business information.",
                    priority="High"
                ),
                Action(
                    title="Review Risks",
                    description="Perform a detailed risk assessment.",
                    priority="Medium"
                )
            ])

        else:

            actions.append(
                Action(
                    title="Do Not Proceed",
                    description="Current evidence does not support this strategy.",
                    priority="High"
                )
            )

        return actions