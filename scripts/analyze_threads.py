from pathlib import Path
import os

# Set paths
WORKSPACE_ROOT = Path(os.getcwd())
if WORKSPACE_ROOT.name == "scripts":
    WORKSPACE_ROOT = WORKSPACE_ROOT.parent

GML_PATH = WORKSPACE_ROOT / "memory/semantic/knowledge_graph/evolution_graph.gml"
REPORT_PATH = WORKSPACE_ROOT / "memory/COMMON_THREADS_REPORT.md"
