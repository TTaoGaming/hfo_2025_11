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
