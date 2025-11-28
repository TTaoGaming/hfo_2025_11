# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 9d889e9b-691e-427d-8b17-aec5363ee22b
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.303654Z'
#     generation: 51
#   topos:
#     address: brain/mission_audit_weave.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: mission_audit_weave.feature
#
---
owner: Swarmlord
status: Placeholder
title: Mission Audit Weave
type: Intent
---

Feature: Knowledge Graph Weaving & Audit
  As the Swarmlord
  I want to weave the individual memory crystals into a cohesive Knowledge Graph
  So that I can query the collective wisdom and identify gaps (orphans/hallucinations).

  Scenario: Weaving the Graph
    Given a directory of Markdown files in "memory/semantic/library/"
    When the "Weaver Ant" scans the directory
    Then it should extract "YAML Frontmatter" (Metadata)
    And it should extract "WikiLinks" (Edges)
    And it should build a "NetworkX" graph
    And it should identify "Orphan Nodes" (No connections)
    And it should identify "Broken Links" (Target missing)
    And it should save the graph to "memory/semantic/knowledge_graph.json"
    And it should generate an audit report in "venom/audit_report.md".
