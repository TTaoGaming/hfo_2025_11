"""
---
holon:
  id: hfo-b88f8406
  type: implementation
  file: research_workflow.py
  status: active
---
"""
import os
import json
import datetime
from ..research_agent import ResearchAgent

class ResearchWorkflow:
    """
    Orchestrates the Research Process.
    """
    def __init__(self):
        self.agent = ResearchAgent()
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "digest")
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, topic: str) -> dict:
        """
        Runs the research agent on a topic.
        """
        print(f"🚀 Starting Research Workflow on: {topic}")
        result = self.agent.research(topic)
        
        artifact = {
            "topic": topic,
            "result": result,
            "timestamp": datetime.datetime.now().isoformat(),
            "agent": "ResearchAgent_Gen63"
        }
        return artifact

    def save_artifact(self, artifact: dict):
        """
        Saves the research artifact to disk.
        """
        filename = f"research_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, "w") as f:
            json.dump(artifact, f, indent=2)
            
        print(f"💾 Artifact saved to: {filepath}")
