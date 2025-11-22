from typing import List, Optional
from pydantic import BaseModel, Field

"""
🦅 Hive Fleet Obsidian: Cognitive Tools
Intent: Provides internal reasoning tools (Sequential Thinking).
Linked to: brain/capability_external_tools.feature
"""


class SequentialThinkingStep(BaseModel):
    thought: str = Field(..., description="The thought content")
    needs_more_time: bool = Field(
        ..., description="Does the agent need more time to think?"
    )
    next_step_hint: Optional[str] = Field(
        None, description="Hint for the next thinking step"
    )


class SequentialThinkingTool:
    """
    A tool that allows the agent to think sequentially, breaking down complex problems.
    This is a 'cognitive' tool that doesn't affect the external world but refines the internal state.
    """

    def __init__(self):
        self.history: List[SequentialThinkingStep] = []

    def think(
        self, thought: str, needs_more_time: bool, next_step_hint: Optional[str] = None
    ) -> str:
        """
        Records a thinking step.
        """
        step = SequentialThinkingStep(
            thought=thought,
            needs_more_time=needs_more_time,
            next_step_hint=next_step_hint,
        )
        self.history.append(step)

        return f"Thought recorded. Total steps: {len(self.history)}. Needs more time: {needs_more_time}"

    def get_thought_process(self) -> str:
        return "\n".join(
            [f"{i+1}. {step.thought}" for i, step in enumerate(self.history)]
        )
