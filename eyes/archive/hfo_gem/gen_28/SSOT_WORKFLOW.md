# SSOT-Driven Workflow (Generation 28)

**Philosophy**: Work upstream (vision/SSOT), let AI swarms generate downstream (code/docs/tests).

---

## 🎯 The Three Sources of Truth

### 1. **Strategic Intent** (`hfo_todo/*.md`, `AGENTS.md`)
- Daily mission planning
- Agent ritual notes
- Gap analysis
- Priority decisions

**You edit these directly** - they capture your vision and decisions.

### 2. **System Model** (`hfo_gem/gen_28/ssot/HFO_SSOT.sysml`)
- SysML v2 single source of truth
- Requirements, use cases, architecture
- Ports, connectors, workflows
- Behavior definitions

**You edit this via SysML tooling** - it's the authoritative model.

### 3. **Execution Policy** (`AGENTS.md` - Swarmlord charter section)
- PREY loop orchestration rules
- Tooling authority matrix
- MCP server trust policies
- Resource management guardrails

**You edit this when doctrine changes** - it governs swarm behavior.

---

## 🔄 The Workflow Loop

```
┌─────────────────────────────────────────────────────────────┐
│ UPSTREAM (You Work Here)                                    │
│                                                              │
│  1. Update TODO with today's mission                        │
│  2. Dictate vision updates to vision_level_diagrams.md      │
│  3. Model changes in HFO_SSOT.sysml (SysML v2)              │
│  4. Update AGENTS.md if policy/tooling changes              │
│                                                              │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│ CODEGEN TRIGGER (AI Swarm)                                  │
│                                                              │
│  Run: ./scripts/swarm/generate_from_ssot.sh                 │
│                                                              │
│  Swarm reads:                                               │
│  - HFO_SSOT.sysml (architecture)                            │
│  - vision_level_diagrams.md (intent)                        │
│  - gen_28_todo.md (priorities)                              │
│                                                              │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│ DOWNSTREAM (AI Generates)                                   │
│                                                              │
│  Generated artifacts:                                       │
│  ├── Code (hfo_swarm/*.py, orchestrators)                   │
│  ├── Tests (tests/*.py, integration, load)                  │
│  ├── Docs (API docs, architecture diagrams)                 │
│  ├── Configs (docker-compose, devcontainer, .env.template)  │
│  └── Database migrations (schema updates)                   │
│                                                              │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│ VALIDATION (AI Swarm + You)                                 │
│                                                              │
│  1. AI runs tests (pytest, integration, smoke)              │
│  2. AI checks quorum (3+ agents approve)                    │
│  3. You review critical changes (git diff)                  │
│  4. Commit if approved, rollback if rejected                │
│                                                              │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   ▼
                [Merge to main, deploy, iterate]
```

---

## 📋 Daily Ritual (SSOT-First)

### Morning (10 min)
1. **Read** `hfo_todo/YYYY-MM-DD-*.md` from yesterday
2. **Create** today's TODO: `hfo_todo/2025-11-11-mission.md`
3. **Prioritize** 1-3 items max
4. **Check** AGENTS.md for any alerts/incidents

### Working Session (2-4 hours)
1. **Update SSOT** with new requirements/architecture
   - Open `hfo_gem/gen_28/ssot/HFO_SSOT.sysml` in Jupyter or SysML editor
   - Add/modify requirements, use cases, blocks
   - Export diagrams: `python ssot/export_ssot_diagrams.py --model HFO_SSOT.sysml --output diagrams/`

2. **Dictate vision** changes to `vision_level_diagrams.md`
   - Append new sections (never delete old intent)
   - Update diagram queue table with status

3. **Trigger codegen swarm** (when SSOT is stable)
   ```bash
   ./scripts/swarm/generate_from_ssot.sh
   ```

4. **Review generated code** in git diff
   - Check tests pass
   - Verify quorum approved
   - Merge if good, reject if hallucinated

### Evening (5 min)
1. **Update today's TODO** with outcomes
2. **Commit SSOT changes**: `git commit -am "feat(ssot): add X requirement"`
3. **Snapshot telemetry** if swarm ran (check Postgres missions table)

---

## 🤖 Swarm Code Generation Pattern

### Input: SSOT → Output: Code

**Example: Generate a new agent**

1. **You add to SSOT** (`HFO_SSOT.sysml`):
```sysml
part def SecurityReviewerAgent :> Agent {
  attribute model : String = "deepseek/deepseek-chat";

  requirement def MustCheckVulnerabilities {
    doc /* Scan code for SQL injection, XSS, auth bypasses */
  }

  port input : CodeArtifact;
  port output : SecurityReport;
}
```

2. **Run swarm codegen**:
```bash
./scripts/swarm/generate_agent.sh --agent SecurityReviewerAgent
```

3. **Swarm generates** `hfo_swarm/security_reviewer.py`:
```python
class SecurityReviewerAgent:
    def __init__(self):
        model = os.getenv("MODEL_SECURITY", "deepseek/deepseek-chat")
        self.llm = ChatOpenAI(...)

    def execute(self, state):
        # Generated from SSOT requirement MustCheckVulnerabilities
        prompt = f"Scan this code for SQL injection, XSS, auth bypasses..."
        ...
```

4. **Swarm generates test** `tests/test_security_reviewer.py`:
```python
def test_security_reviewer_finds_sql_injection():
    agent = SecurityReviewerAgent()
    code = "SELECT * FROM users WHERE id = " + user_input
    result = agent.execute({"code": code})
    assert "SQL injection" in result["findings"]
```

5. **You review, approve, commit**

---

## 🛠️ Scripts to Create

### `scripts/swarm/generate_from_ssot.sh`
Main orchestrator - reads SSOT, generates all downstream artifacts.

### `scripts/swarm/generate_agent.sh`
Generates a single agent from SSOT block definition.

### `scripts/swarm/generate_tests.sh`
Generates pytest tests for all agents.

### `scripts/swarm/validate_generated.sh`
Runs tests, quorum check, reports approval.

### `scripts/swarm/sync_ssot_to_db.sh`
Updates Postgres schema to match SSOT model.

---

## 📊 OpenTelemetry Integration

### Current: Simple console logging
Your swarm now has basic tracing (span start/end, timing).

### Next: Export to Jaeger/Tempo
```python
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# In swarm init
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Each agent gets tracer
tracer = trace.get_tracer(__name__)

# Wrap agent execution
with tracer.start_as_current_span("ResearcherAgent.execute") as span:
    span.set_attribute("mission_id", state['mission_id'])
    result = self.llm.invoke(prompt)
    span.set_attribute("tokens_used", result.usage_metadata.total_tokens)
```

### Visualize in Jaeger
```bash
docker run -d -p 16686:16686 -p 4317:4317 jaegertracing/all-in-one:latest
# Open http://localhost:16686 to see traces
```

---

## 🎯 Success Metrics (SSOT-Driven)

### Daily
- [ ] SSOT updated with at least 1 new requirement/block
- [ ] Vision docs synced with SSOT changes
- [ ] Codegen swarm ran at least once
- [ ] Generated code passed tests + quorum

### Weekly
- [ ] SSOT export produces all diagrams without errors
- [ ] All agents have corresponding SSOT blocks
- [ ] Database schema matches SSOT model
- [ ] Zero manual code edits downstream (all via SSOT)

### Monthly
- [ ] SSOT is authoritative source for 100% of architecture
- [ ] Swarm can regenerate entire codebase from SSOT
- [ ] New developers onboard via SSOT reading only
- [ ] Molt shell archived with full SSOT snapshot

---

## 🚨 Anti-Patterns (What NOT to Do)

❌ **Editing generated code directly** - Changes will be lost on next codegen
✅ **Update SSOT, regenerate** - Preserves intent, repeatable

❌ **Creating new files outside swarm** - They won't be in SSOT
✅ **Add to SSOT first, then generate** - Everything traceable

❌ **Manual database migrations** - Schema drift from SSOT
✅ **Model in SSOT, generate migration** - Single source of truth

❌ **Ad-hoc agent experiments** - No lineage, no reproducibility
✅ **Prototype in SSOT, generate agent** - Documented, versioned

---

## 🎁 What This Unlocks

### For You
- Work at vision level (your strength)
- No context-switching to implementation details
- Swarm handles grunt work (boilerplate, tests, docs)

### For the Swarm
- Clear authoritative source (SSOT)
- Validation criteria built-in (requirements)
- Quorum based on SSOT compliance

### For Future You
- SSOT is the documentation
- Regenerate entire system from scratch
- Molt shells preserve exact SSOT state

---

## ⏭️ Next Steps (Today)

1. **Commit the working swarm**:
```bash
git add hfo_swarm/basic_swarm.py .env
git commit -m "feat: first successful swarm run with DeepSeek V3 + telemetry"
```

2. **Create first SSOT codegen script**:
```bash
./scripts/swarm/generate_agent.sh --help
```

3. **Add telemetry export to Jaeger**:
```bash
docker run -d -p 16686:16686 -p 4317:4317 jaegertracing/all-in-one:latest
```

4. **Model your next agent in SSOT**:
   - Open `HFO_SSOT.sysml`
   - Add a new `part def` for your next specialist agent
   - Generate it with the swarm

---

**You now have a working swarm AND the vision for SSOT-driven development. Let's build the codegen scripts next!**
