---
card:
  id: standard-swarmlord-digest-template
  source: standard_swarmlord_digest.md
  type: Tool
---

# 🃏 Swarmlord Digest Template

> **Intuition**: A canonical alchemical triad—digest, map, and spec—that transmutes raw knowledge into an executable cognitive artifact for the second brain.

## 📜 The Incantation (Intent)
```gherkin
Feature: Swarmlord Digest Artifact Generation
  As a Knowledge Architect
  I want to standardize HFO outputs
  So that all artifacts form a cohesive global workspace

  Scenario: Generating a canonical digest from raw content
    Given raw documentation with title, context, and details
    When applying the Swarmlord Digest Template structure
    Then produce a Markdown artifact containing:
      | Section | Content |
      |---------|---------|
      | Executive Summary | BLUF, Matrix table, Strategic Rationale |
      | Visualization | Mermaid diagram (flowchart/sequence/class/mindmap) |
      | Formal Intent | Gherkin Feature with traceability links |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Generator for Swarmlord Digest Markdown
def generate_swarmlord_digest(
    title: str,
    subtitle: str,
    bluf: str,
    matrix_data: list[dict[str, str]],
    mermaid_code: str,
    gherkin_spec: str,
    status: str = "Active",
    octet: str = "Ontos ID | Chronos Date | Telos Purpose"
) -> str:
    matrix_rows = "\n".join([f"| {row['concept']} | {row['value']} | {row['note']} |" for row in matrix_data])
    template = f"""# 🦅 {title}: {subtitle}

> **Status**: {status}
> **Octet**: {octet}

## 1. Executive Summary (Digest)
**BLUF**: {bluf}

### The Matrix
| Concept | Value | Note |
|---------|-------|------|
{matrix_rows}

**Strategic Rationale**:
[Why we are doing this. The trade-offs considered.]

---

## 2. Visualization (Map)
```mermaid
{mermaid_code}
```

---

## 3. Formal Intent (Spec)
{gherkin_spec}
"""
    return template
```

## ⚔️ Synergies
*   **Gherkin Integration**: Embeds BDD specs as the executable "Intent" layer, traceable to implementation code.
*   **Mermaid Visualization**: Leverages diagrams for intuitive mapping of flows, architectures, or concepts.
*   **Hexagon Metadata**: Aligns with ontos/chronos/topos/telos for versioning, location, and purpose tracking.
*   **HFO Ecosystem**: Serves as the canonical output format for Hive-mind Fractal Outputs, enabling fractal knowledge scaling.
*   **Second Brain**: Composes with Grimoire Cards and other standards for a unified cognitive workspace.