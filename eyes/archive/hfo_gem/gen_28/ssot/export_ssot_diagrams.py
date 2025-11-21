#!/usr/bin/env python3
"""Generate Mermaid diagrams from the HFO SSOT textual model."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ACTION_PATTERN = re.compile(r"^\s*action\s+([A-Za-z0-9_]+)\b")
FLOW_PATTERN = re.compile(
    r"^\s*succession\s+flow\s+([A-Za-z0-9_]+)\s+from\s+([A-Za-z0-9_.]+)\s+to\s+([A-Za-z0-9_.]+);"
)
PART_DEF_PATTERN = re.compile(r"^\s*part\s+def\s+([A-Za-z0-9_]+)\b")
PORT_DEF_PATTERN = re.compile(r"^\s*port\s+def\s+([A-Za-z0-9_]+)\b")
ATTRIBUTE_PATTERN = re.compile(
    r"^\s*attribute\s+([A-Za-z0-9_]+)\s*:\s*([A-Za-z0-9_]+);"
)
PART_USAGE_PATTERN = re.compile(r"^\s*part\s+([A-Za-z0-9_]+)\s*:\s*([A-Za-z0-9_]+);")
PORT_USAGE_PATTERN = re.compile(r"^\s*port\s+([A-Za-z0-9_]+)\s*:\s*([A-Za-z0-9_]+);")
REQUIREMENT_PATTERN = re.compile(r"^\s*requirement\s+([A-Za-z0-9_]+)\s*{")
REQUIREMENT_ID_PATTERN = re.compile(r"^\s*id\s*=\s*\"([^\"]+)\"")
REQUIREMENT_TEXT_PATTERN = re.compile(r"^\s*text\s*=\s*\"([^\"]*)\"")
CONNECTOR_COMMENT_PATTERN = re.compile(
    r"^\s*//\s*connect\s+([A-Za-z0-9_]+)\s+([A-Za-z0-9_.]+)\s*->\s*([A-Za-z0-9_.]+)"
)
SATISFY_COMMENT_PATTERN = re.compile(
    r"^\s*//\s*satisfy\s+([A-Za-z0-9_]+)\s+by\s+([A-Za-z0-9_:.]+)"
)

MERMAID_INIT_DIRECTIVE = "%%{init: {'themeVariables': {'fontSize': '18px', 'lineHeight': '26px', 'fontFamily': 'Inter, Arial, sans-serif'}}}%%"


@dataclass
class ActionNode:
    name: str
    parent: Optional[str]

    @property
    def label(self) -> str:
        return humanize(self.name)


@dataclass
class FlowEdge:
    name: str
    source: str
    target: str

    @property
    def source_action(self) -> str:
        return self.source.split(".")[0]

    @property
    def target_action(self) -> str:
        return self.target.split(".")[0]

    @property
    def label(self) -> str:
        src_feature = self.source.split(".")[-1]
        dst_feature = self.target.split(".")[-1]
        if src_feature == dst_feature:
            return src_feature
        return f"{src_feature} → {dst_feature}"


@dataclass
class PartDef:
    name: str
    attributes: List[Tuple[str, str]]


@dataclass
class PortDef:
    name: str
    attributes: List[Tuple[str, str]]


@dataclass
class PartUsage:
    role: str
    part_type: str


@dataclass
class PortInstance:
    role: str
    port_type: str


@dataclass
class Connector:
    name: str
    source: str
    target: str


@dataclass
class Requirement:
    name: str
    req_id: Optional[str]
    text: Optional[str]


@dataclass
class RequirementSatisfaction:
    requirement: str
    target: str


def humanize(identifier: str) -> str:
    if "_" in identifier:
        parts = identifier.split("_")
        return " ".join(p.capitalize() for p in parts if p)

    result: List[str] = []
    word: List[str] = []
    for char in identifier:
        if char.isupper() and word:
            result.append("".join(word))
            word = [char]
        else:
            word.append(char)
    if word:
        result.append("".join(word))
    title = " ".join(result)
    title = re.sub(r"(?<=\D)(\d+)", r" \1", title)
    return title.replace("  ", " ").strip()


def sanitize_mermaid_id(identifier: str) -> str:
    return re.sub(r"[^A-Za-z0-9_]", "_", identifier)


def parse_model(text: str) -> Tuple[Dict[str, ActionNode], List[FlowEdge]]:
    actions: Dict[str, ActionNode] = {}
    flows: List[FlowEdge] = []

    curly_depth = 0
    stack: List[Tuple[str, int]] = []

    for raw_line in text.splitlines():
        action_match = ACTION_PATTERN.match(raw_line)
        if action_match:
            action_name = action_match.group(1)
            parent = stack[-1][0] if stack else None
            actions[action_name] = ActionNode(name=action_name, parent=parent)
            stack.append((action_name, curly_depth))

        flow_match = FLOW_PATTERN.match(raw_line)
        if flow_match:
            flow_name, source, target = flow_match.groups()
            flows.append(FlowEdge(name=flow_name, source=source, target=target))

        curly_depth += raw_line.count("{")
        curly_depth -= raw_line.count("}")

        while stack and curly_depth <= stack[-1][1]:
            stack.pop()

    return actions, flows


def parse_structures(
    text: str,
) -> Tuple[
    Dict[str, PartDef],
    Dict[str, List[PartUsage]],
    Dict[str, PortDef],
    Dict[str, List[PortInstance]],
    List[Connector],
    List[RequirementSatisfaction],
]:
    part_defs: Dict[str, PartDef] = {}
    assemblies: Dict[str, List[PartUsage]] = {}
    port_defs: Dict[str, PortDef] = {}
    port_usages: Dict[str, List[PortInstance]] = {}
    connectors: List[Connector] = []
    satisfactions: List[RequirementSatisfaction] = []

    curly_depth = 0
    stack: List[Tuple[str, int, str]] = []

    for raw_line in text.splitlines():
        part_def_match = PART_DEF_PATTERN.match(raw_line)
        if part_def_match:
            part_name = part_def_match.group(1)
            part_defs.setdefault(part_name, PartDef(name=part_name, attributes=[]))
            assemblies.setdefault(part_name, [])
            port_usages.setdefault(part_name, [])
            stack.append((part_name, curly_depth, "part"))

        port_def_match = PORT_DEF_PATTERN.match(raw_line)
        if port_def_match:
            port_name = port_def_match.group(1)
            port_defs.setdefault(port_name, PortDef(name=port_name, attributes=[]))
            stack.append((port_name, curly_depth, "port"))

        attr_match = ATTRIBUTE_PATTERN.match(raw_line)
        if attr_match and stack:
            attr_name, attr_type = attr_match.groups()
            current_name, _, kind = stack[-1]
            if kind == "part":
                part_defs[current_name].attributes.append((attr_name, attr_type))
            elif kind == "port":
                port_defs[current_name].attributes.append((attr_name, attr_type))

        part_usage_match = PART_USAGE_PATTERN.match(raw_line)
        if part_usage_match and stack:
            role, part_type = part_usage_match.groups()
            current_name, _, kind = stack[-1]
            if kind == "part":
                assemblies.setdefault(current_name, []).append(
                    PartUsage(role=role, part_type=part_type)
                )

        port_usage_match = PORT_USAGE_PATTERN.match(raw_line)
        if port_usage_match and stack:
            role, port_type = port_usage_match.groups()
            current_name, _, kind = stack[-1]
            if kind == "part":
                port_usages.setdefault(current_name, []).append(
                    PortInstance(role=role, port_type=port_type)
                )

        connector_match = CONNECTOR_COMMENT_PATTERN.match(raw_line)
        if connector_match:
            name, source, target = connector_match.groups()
            connectors.append(Connector(name=name, source=source, target=target))

        satisfy_match = SATISFY_COMMENT_PATTERN.match(raw_line)
        if satisfy_match:
            requirement, target = satisfy_match.groups()
            satisfactions.append(
                RequirementSatisfaction(requirement=requirement, target=target)
            )

        curly_depth += raw_line.count("{")
        curly_depth -= raw_line.count("}")

        while stack and curly_depth <= stack[-1][1]:
            stack.pop()

    assemblies = {name: usages for name, usages in assemblies.items() if usages}
    port_usages = {name: usages for name, usages in port_usages.items() if usages}

    return part_defs, assemblies, port_defs, port_usages, connectors, satisfactions


def parse_requirements(text: str) -> Dict[str, Requirement]:
    requirements: Dict[str, Requirement] = {}
    curly_depth = 0
    stack: List[Tuple[str, int]] = []

    for raw_line in text.splitlines():
        req_match = REQUIREMENT_PATTERN.match(raw_line)
        if req_match:
            req_name = req_match.group(1)
            requirements[req_name] = Requirement(name=req_name, req_id=None, text=None)
            stack.append((req_name, curly_depth))

        if stack:
            current_req = stack[-1][0]
            id_match = REQUIREMENT_ID_PATTERN.match(raw_line)
            if id_match:
                requirements[current_req].req_id = id_match.group(1)

            text_match = REQUIREMENT_TEXT_PATTERN.match(raw_line)
            if text_match:
                requirements[current_req].text = text_match.group(1)

        curly_depth += raw_line.count("{")
        curly_depth -= raw_line.count("}")

        while stack and curly_depth <= stack[-1][1]:
            stack.pop()

    return requirements


FLOW_ORDER = [
    "CaptureIntent",
    "ClarifyMission1",
    "ClarifyMission2",
    "SelectWorkflow",
    "PublishMissionIntent",
    "DeployOrchestration",
    "CoordinateSwarm",
    "ValidateResults",
    "DeliverOutcome",
    "UpdateKnowledge",
]


def render_mermaid_flow(actions: Dict[str, ActionNode], flows: List[FlowEdge]) -> str:
    lifecycle_children = [
        node for node in actions.values() if node.parent == "MissionLifecycle"
    ]
    order_index = {name: idx for idx, name in enumerate(FLOW_ORDER)}
    lifecycle_children.sort(
        key=lambda node: (order_index.get(node.name, len(order_index)), node.name)
    )

    lines = [
        "```mermaid",
        MERMAID_INIT_DIRECTIVE,
        "flowchart TD",
        "    classDef step fill:#0d3b66,stroke:#0d3b66,stroke-width:1px,color:#ffffff",
    ]

    for node in lifecycle_children:
        lines.append(f'    {node.name}["{node.label}"]:::step')

    if flows:
        lines.append("")
    for flow in flows:
        if flow.source_action not in actions or flow.target_action not in actions:
            continue
        if (
            actions[flow.source_action].parent != "MissionLifecycle"
            or actions[flow.target_action].parent != "MissionLifecycle"
        ):
            continue
        lines.append(f"    {flow.source_action} -->|{flow.label}| {flow.target_action}")

    lines.append("```")
    return "\n".join(lines)


def render_mermaid_sequence(flows: List[FlowEdge]) -> str:
    ordered_actions = FLOW_ORDER

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "sequenceDiagram"]
    lines.append("    autonumber")

    label_map = {name: humanize(name) for name in ordered_actions}
    for name in ordered_actions:
        lines.append(f"    participant {name} as {label_map[name]}")

    for idx, name in enumerate(ordered_actions[:-1]):
        successors = [flow for flow in flows if flow.source_action == name]
        if not successors:
            continue
        next_name = ordered_actions[idx + 1]
        chosen = None
        for flow in successors:
            if flow.target_action == next_name:
                chosen = flow
                break
        if not chosen:
            chosen = successors[0]
        lines.append(f"    {name}->>{chosen.target_action}: {chosen.label}")

    lines.append("```")
    return "\n".join(lines)


def render_mermaid_state(actions: Dict[str, ActionNode], flows: List[FlowEdge]) -> str:
    lifecycle_children = [
        node for node in actions.values() if node.parent == "MissionLifecycle"
    ]
    if not lifecycle_children:
        return "_No mission lifecycle actions detected._"

    present = [name for name in FLOW_ORDER if name in actions]

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "stateDiagram-v2"]
    if present:
        lines.append(f"    [*] --> {present[0]}")
        for idx, name in enumerate(present):
            label = humanize(name)
            lines.append(f'    state "{label}" as {name}')
            if idx < len(present) - 1:
                lines.append(f"    {name} --> {present[idx + 1]}")
        lines.append(f"    {present[-1]} --> [*]")
    lines.append("```")
    return "\n".join(lines)


def render_mermaid_bdd(
    part_defs: Dict[str, PartDef], assemblies: Dict[str, List[PartUsage]]
) -> str:
    if not part_defs:
        return "_No part definitions detected in the SSOT model._"

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "classDiagram"]

    for name in sorted(part_defs.keys()):
        part = part_defs[name]
        lines.append(f"    class {name} {{")
        if part.attributes:
            for attr_name, attr_type in part.attributes:
                lines.append(f"        +{attr_name} : {attr_type}")
        else:
            lines.append("        ...")
        lines.append("    }")

    for assembly_name in sorted(assemblies.keys()):
        for usage in assemblies[assembly_name]:
            lines.append(f"    {assembly_name} *-- {usage.part_type} : {usage.role}")

    lines.append("```")
    return "\n".join(lines)


def render_mermaid_component(assemblies: Dict[str, List[PartUsage]]) -> str:
    if not assemblies:
        return "_No assemblies captured in the SSOT model._"

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "graph LR"]
    for assembly_name, usages in assemblies.items():
        lines.append(f"    {assembly_name}{{{assembly_name}}}")
        for usage in usages:
            lines.append(f"    {assembly_name} -->|{usage.role}| {usage.part_type}")

    lines.append("```")
    return "\n".join(lines)


def render_mermaid_structure_mindmap(assemblies: Dict[str, List[PartUsage]]) -> str:
    if not assemblies:
        return "_No assemblies captured in the SSOT model._"

    def escape(text: str) -> str:
        return text.replace('"', "'")

    lines = [
        "```mermaid",
        MERMAID_INIT_DIRECTIVE,
        "mindmap",
        "  SwarmlordAssemblies((Swarmlord Assemblies))",
    ]
    for assembly_name, usages in assemblies.items():
        lines.append(f"    {escape(assembly_name)}")
        for usage in usages:
            lines.append(f"      {escape(usage.role)}: {escape(usage.part_type)}")

    lines.append("```")
    return "\n".join(lines)


def render_structure_table(part_defs: Dict[str, PartDef]) -> str:
    if not part_defs:
        return "_No structural parts captured._"

    lines = ["| Part | Attributes |", "| --- | --- |"]
    for name in sorted(part_defs.keys()):
        part = part_defs[name]
        if part.attributes:
            attr_text = "<br>".join(
                f"{attr}: {attr_type}" for attr, attr_type in part.attributes
            )
        else:
            attr_text = "—"
        lines.append(f"| {name} | {attr_text} |")

    return "\n".join(lines)


def render_port_definition_table(port_defs: Dict[str, PortDef]) -> str:
    if not port_defs:
        return "_No ports defined in the SSOT model._"

    lines = ["| Port | Attributes |", "| --- | --- |"]
    for name in sorted(port_defs.keys()):
        port = port_defs[name]
        if port.attributes:
            attr_text = "<br>".join(
                f"{attr}: {attr_type}" for attr, attr_type in port.attributes
            )
        else:
            attr_text = "—"
        lines.append(f"| {name} | {attr_text} |")

    return "\n".join(lines)


def render_port_usage_table(port_usages: Dict[str, List[PortInstance]]) -> str:
    if not port_usages:
        return "_No port usages captured in the SSOT model._"

    lines = ["| Part | Ports |", "| --- | --- |"]
    for part_name in sorted(port_usages.keys()):
        entries = port_usages[part_name]
        port_text = "<br>".join(f"{entry.role}: {entry.port_type}" for entry in entries)
        lines.append(f"| {part_name} | {port_text} |")

    return "\n".join(lines)


def render_connector_graph(connectors: List[Connector]) -> str:
    if not connectors:
        return "_No connectors annotated in the SSOT model._"

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "graph LR"]
    node_ids: Dict[str, str] = {}

    for connector in connectors:
        for endpoint in (connector.source, connector.target):
            if endpoint not in node_ids:
                node_id = sanitize_mermaid_id(endpoint)
                node_ids[endpoint] = node_id
                lines.append(f'    {node_id}["{endpoint}"]')
        src_id = node_ids[connector.source]
        dst_id = node_ids[connector.target]
        lines.append(f"    {src_id} ---|{connector.name}| {dst_id}")

    lines.append("```")
    return "\n".join(lines)


def render_connector_table(connectors: List[Connector]) -> str:
    if not connectors:
        return "_No connectors annotated in the SSOT model._"

    lines = ["| Connector | Source | Target |", "| --- | --- | --- |"]
    for connector in connectors:
        lines.append(f"| {connector.name} | {connector.source} | {connector.target} |")

    return "\n".join(lines)


def render_requirements_table(requirements: Dict[str, Requirement]) -> str:
    if not requirements:
        return "_No requirements detected in the SSOT model._"

    lines = ["| Name | ID | Text |", "| --- | --- | --- |"]
    for name in sorted(requirements.keys()):
        req = requirements[name]
        req_id = req.req_id or "—"
        text = (req.text or "—").replace("|", "\\|")
        lines.append(f"| {name} | {req_id} | {text} |")

    return "\n".join(lines)


def truncate(text: str, limit: int = 72) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def render_requirement_graph(requirements: Dict[str, Requirement]) -> str:
    if not requirements:
        return "_No requirements detected in the SSOT model._"

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "graph TD", "    Root[Requirements]"]
    for name in sorted(requirements.keys()):
        req = requirements[name]
        label_parts = [req.req_id or name]
        if req.text:
            label_parts.append(truncate(req.text, 60))
        label = "\\n".join(label_parts).replace('"', "'")
        node_name = f"Req_{name}"
        lines.append(f'    {node_name}["{label}"]')
        lines.append(f"    Root --> {node_name}")

    lines.append("```")
    return "\n".join(lines)


def render_requirement_mindmap(requirements: Dict[str, Requirement]) -> str:
    if not requirements:
        return "_No requirements detected in the SSOT model._"

    def escape(text: str) -> str:
        return text.replace('"', "'")

    lines = [
        "```mermaid",
        MERMAID_INIT_DIRECTIVE,
        "mindmap",
        "  RequirementsRoot((Requirements))",
    ]
    for name in sorted(requirements.keys()):
        req = requirements[name]
        node_label = req.req_id or name
        lines.append(f"    {escape(node_label)}")
        if req.text:
            lines.append(f"      Detail: {escape(truncate(req.text, 80))}")

    lines.append("```")
    return "\n".join(lines)


def render_satisfaction_table(satisfactions: List[RequirementSatisfaction]) -> str:
    if not satisfactions:
        return "_No requirement satisfaction annotations present._"

    lines = ["| Requirement | Satisfied By |", "| --- | --- |"]
    for sat in satisfactions:
        lines.append(f"| {sat.requirement} | {sat.target} |")

    return "\n".join(lines)


def render_satisfaction_graph(
    requirements: Dict[str, Requirement], satisfactions: List[RequirementSatisfaction]
) -> str:
    if not satisfactions:
        return "_No requirement satisfaction annotations present._"

    lines = ["```mermaid", MERMAID_INIT_DIRECTIVE, "graph LR"]
    target_nodes: Dict[str, str] = {}
    requirement_nodes: Dict[str, str] = {}

    for sat in satisfactions:
        req = requirements.get(sat.requirement)
        req_label = req.req_id if req and req.req_id else sat.requirement
        if sat.requirement not in requirement_nodes:
            req_node = sanitize_mermaid_id(f"REQ_{sat.requirement}")
            requirement_nodes[sat.requirement] = req_node
            lines.append(f'    {req_node}["{req_label}"]')
        else:
            req_node = requirement_nodes[sat.requirement]

        if sat.target not in target_nodes:
            target_node = sanitize_mermaid_id(sat.target)
            target_nodes[sat.target] = target_node
            lines.append(f'    {target_node}["{sat.target}"]')
        else:
            target_node = target_nodes[sat.target]

        lines.append(f"    {target_node} --> {req_node}")

    lines.append("```")
    return "\n".join(lines)


def build_markdown(
    actions: Dict[str, ActionNode],
    flows: List[FlowEdge],
    part_defs: Dict[str, PartDef],
    assemblies: Dict[str, List[PartUsage]],
    requirements: Dict[str, Requirement],
    port_defs: Dict[str, PortDef],
    port_usages: Dict[str, List[PortInstance]],
    connectors: List[Connector],
    satisfactions: List[RequirementSatisfaction],
) -> str:
    flowchart = render_mermaid_flow(actions, flows)
    sequence = render_mermaid_sequence(flows)
    state_diagram = render_mermaid_state(actions, flows)
    bdd = render_mermaid_bdd(part_defs, assemblies)
    component = render_mermaid_component(assemblies)
    port_def_table = render_port_definition_table(port_defs)
    port_usage_table = render_port_usage_table(port_usages)
    connector_graph = render_connector_graph(connectors)
    connector_table = render_connector_table(connectors)
    structure_mindmap = render_mermaid_structure_mindmap(assemblies)
    structure_table = render_structure_table(part_defs)
    requirements_table = render_requirements_table(requirements)
    requirement_graph = render_requirement_graph(requirements)
    requirement_mindmap = render_requirement_mindmap(requirements)
    satisfaction_table = render_satisfaction_table(satisfactions)
    satisfaction_graph = render_satisfaction_graph(requirements, satisfactions)

    return "\n".join(
        [
            "# Hive Fleet Obsidian SSOT – Visualizations",
            "",
            "<!-- Generated by export_ssot_diagrams.py -->",
            "",
            "## Mission Lifecycle",
            "",
            "### Flowchart",
            "",
            flowchart,
            "",
            "### Sequence",
            "",
            sequence,
            "",
            "### State Progression",
            "",
            state_diagram,
            "",
            "## Structural Blocks",
            "",
            "### Block Definition Diagram",
            "",
            bdd,
            "",
            "### Assembly View",
            "",
            component,
            "",
            "### Port Definitions",
            "",
            port_def_table,
            "",
            "### Part Port Summary",
            "",
            port_usage_table,
            "",
            "### Connector View",
            "",
            connector_graph,
            "",
            "### Connector Table",
            "",
            connector_table,
            "",
            "### Structural Mindmap",
            "",
            structure_mindmap,
            "",
            "### Attribute Summary",
            "",
            structure_table,
            "",
            "## Requirements",
            "",
            "### Table",
            "",
            requirements_table,
            "",
            "### Relationship Graph",
            "",
            requirement_graph,
            "",
            "### Requirement Mindmap",
            "",
            requirement_mindmap,
            "",
            "### Satisfaction Table",
            "",
            satisfaction_table,
            "",
            "### Satisfaction Graph",
            "",
            satisfaction_graph,
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export Mermaid diagrams from the HFO SSOT model"
    )
    parser.add_argument(
        "--model",
        default="HFO_SSOT.sysml",
        help="Path to the SysML v2 SSOT source file (default: HFO_SSOT.sysml)",
    )
    parser.add_argument(
        "--output",
        default="HFO_SSOT_diagrams.md",
        help="Markdown file to write (default: HFO_SSOT_diagrams.md)",
    )
    args = parser.parse_args()

    model_path = Path(args.model)
    if not model_path.exists():
        raise SystemExit(f"Model file not found: {model_path}")

    model_text = model_path.read_text(encoding="utf-8")
    actions, flows = parse_model(model_text)
    (
        part_defs,
        assemblies,
        port_defs,
        port_usages,
        connectors,
        satisfactions,
    ) = parse_structures(model_text)
    requirements = parse_requirements(model_text)

    if not actions:
        raise SystemExit(
            "No actions detected in the model. Is the file formatted as expected?"
        )

    output_text = build_markdown(
        actions,
        flows,
        part_defs,
        assemblies,
        requirements,
        port_defs,
        port_usages,
        connectors,
        satisfactions,
    )
    output_path = Path(args.output)
    output_path.write_text(output_text, encoding="utf-8")

    print(f"Wrote Mermaid diagrams to {output_path}")


if __name__ == "__main__":
    main()
