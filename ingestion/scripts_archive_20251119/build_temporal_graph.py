import os
import re
import json
import networkx as nx
from pathlib import Path
from collections import defaultdict

# Configuration
STAGING_DIR = Path("hive_fleet_obsidian_2025_11/ingestion/staging_memory")
OUTPUT_DIR = Path("hive_fleet_obsidian_2025_11/ingestion/graph_data")
OUTPUT_METADATA = OUTPUT_DIR / "temporal_metadata.json"
OUTPUT_GRAPH = OUTPUT_DIR / "evolution_graph.gml"

def extract_gen_from_path(path_parts):
    """
    Extracts generation number from path parts.
    Prioritizes explicit 'gen_X' folders.
    """
    for part in path_parts:
        # Match gen_1, gen_12, Gen 50, etc.
        match = re.search(r'(?:gen|Gen)[_\-\s]?(\d+)', part)
        if match:
            return int(match.group(1))
    return None

def normalize_concept_name(filename):
    """
    Normalizes filenames to identify the same concept across generations.
    e.g., 'agent_v1.py' -> 'agent', 'agent.py' -> 'agent'
    """
    name = filename.lower()
    # Remove extensions
    name = os.path.splitext(name)[0]
    # Remove version suffixes like _v1, _final, _copy
    name = re.sub(r'[_\-\s]v\d+', '', name)
    name = re.sub(r'[_\-\s]final', '', name)
    return name

def build_graph():
    print(f"Scanning {STAGING_DIR} for Temporal Graph construction...")
    
    # Data Structures
    timeline = defaultdict(list) # Gen -> [Files]
    concepts = defaultdict(list) # ConceptName -> [{gen, path}]
    G = nx.DiGraph()

    file_count = 0
    
    for root, dirs, files in os.walk(STAGING_DIR):
        for filename in files:
            if filename.endswith(('.md', '.py', '.json', '.txt')):
                file_path = Path(root) / filename
                rel_path = file_path.relative_to(STAGING_DIR)
                
                gen = extract_gen_from_path(rel_path.parts)
                
                if gen is not None:
                    concept_name = normalize_concept_name(filename)
                    
                    node_id = str(rel_path)
                    
                    # Add to indices
                    timeline[gen].append(node_id)
                    concepts[concept_name].append({
                        "gen": gen,
                        "path": str(rel_path),
                        "filename": filename
                    })
                    
                    # Add Node to Graph
                    G.add_node(node_id, gen=gen, concept=concept_name, filename=filename)
                    
                    file_count += 1

    print(f"Indexed {file_count} files across {len(timeline)} generations.")
    print(f"Identified {len(concepts)} unique concepts.")

    # Build Edges (Evolutionary Links)
    edge_count = 0
    for concept, versions in concepts.items():
        # Sort versions by generation
        sorted_versions = sorted(versions, key=lambda x: x['gen'])
        
        # Link Gen N -> Gen N+1
        for i in range(len(sorted_versions) - 1):
            v_current = sorted_versions[i]
            v_next = sorted_versions[i+1]
            
            # Only link if they are different files
            if v_current['path'] != v_next['path']:
                G.add_edge(v_current['path'], v_next['path'], type="evolution")
                edge_count += 1

    print(f"Created {edge_count} evolutionary edges.")

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save Metadata
    metadata = {
        "stats": {
            "files": file_count,
            "generations": len(timeline),
            "concepts": len(concepts),
            "edges": edge_count
        },
        "timeline": dict(sorted(timeline.items())), # Sorted by Gen
        "concepts": dict(concepts)
    }
    
    with open(OUTPUT_METADATA, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"Saved metadata to {OUTPUT_METADATA}")

    # Save Graph (GML format for visualization/analysis)
    nx.write_gml(G, OUTPUT_GRAPH)
    print(f"Saved graph to {OUTPUT_GRAPH}")

if __name__ == "__main__":
    build_graph()
