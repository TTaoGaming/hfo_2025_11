import sqlite3
import json
import os

DB_PATH = "buds/hfo_gem_gen_58/memory/hfo_memory.db"
REPORT_PATH = "buds/hfo_gem_gen_58/reports/Holographic_Quorum_Report.md"

def generate_report():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Get the Original File (Memory Item)
    # We'll just grab the last one for now, which should be test_protocol.md
    cursor.execute("SELECT source_path, content, content_hash FROM memory_items ORDER BY id DESC LIMIT 1")
    item = cursor.fetchone()
    if not item:
        print("No memory items found.")
        return

    source_path, content, content_hash = item
    
    md_content = f"# 🦅 Holographic Quorum Report\n\n"
    md_content += f"**Source**: `{source_path}`\n"
    md_content += f"**Hash**: `{content_hash}`\n\n"
    md_content += "## 1. Original Input\n\n"
    md_content += "```markdown\n"
    md_content += content
    md_content += "\n```\n\n"
    
    # 2. Get Level 0 Artifacts (The 8 Outputs)
    cursor.execute("SELECT agent_id, model_used, pillars_json FROM level0_artifacts WHERE source_hash = ? ORDER BY agent_id ASC", (content_hash,))
    l0_rows = cursor.fetchall()
    
    md_content += "## 2. The Council of Eight (Level 0 Artifacts)\n\n"
    
    for row in l0_rows:
        agent_id, model, pillars_json = row
        pillars = json.loads(pillars_json)
        
        md_content += f"### 🕷️ Agent {agent_id} ({model})\n\n"
        
        # Create a table for the 8 pillars
        md_content += "| Pillar | Summary | Confidence |\n"
        md_content += "| :--- | :--- | :--- |\n"
        
        for pillar_name, data in pillars.items():
            summary = data.get('summary', '').replace('\n', ' ')
            confidence = data.get('confidence', 0.0)
            md_content += f"| **{pillar_name.capitalize()}** | {summary} | {confidence} |\n"
        
        md_content += "\n"

    # 3. Get Level 1 Artifact (The Synthesis)
    cursor.execute("SELECT consensus_score, synthesis, resolved_conflicts, model_used FROM level1_artifacts WHERE source_hash = ? ORDER BY id DESC LIMIT 1", (content_hash,))
    l1_row = cursor.fetchone()
    
    if l1_row:
        score, synthesis, conflicts_json, model = l1_row
        conflicts = json.loads(conflicts_json)
        
        md_content += "## 3. The Swarmlord's Decree (Level 1 Artifact)\n\n"
        md_content += f"**Synthesizer**: `{model}`\n"
        md_content += f"**Consensus Score**: `{score}`\n\n"
        
        md_content += "### 🔮 The Synthesis\n"
        md_content += f"{synthesis}\n\n"
        
        if conflicts:
            md_content += "### ⚔️ Resolved Conflicts\n"
            for c in conflicts:
                md_content += f"- {c}\n"
    else:
        md_content += "## 3. The Swarmlord's Decree\n\n*No Level 1 Artifact found (Quorum failed?)*\n"

    # Write to file
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w") as f:
        f.write(md_content)
    
    print(f"Report generated at: {REPORT_PATH}")
    conn.close()

if __name__ == "__main__":
    generate_report()
