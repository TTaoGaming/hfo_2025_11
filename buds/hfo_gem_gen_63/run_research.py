import sys
import os

# Add the workspace root to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from buds.hfo_gem_gen_63.src.workflows.research_workflow import ResearchWorkflow

def main():
    topic = "The future of agentic coding frameworks 2025"
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    
    print(f"Running Research Workflow for: {topic}")
    wf = ResearchWorkflow()
    artifact = wf.run(topic)
    wf.save_artifact(artifact)
    print("Done.")

if __name__ == "__main__":
    main()
