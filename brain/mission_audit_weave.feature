# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: e1374d1f-7d8c-45ea-baea-066fc48c14a3
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:31.467089+00:00'
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
