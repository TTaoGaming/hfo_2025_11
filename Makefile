.PHONY: test-all test-ray test-temporal test-nats test-instructor test-langgraph test-langsmith test-pgvector

PYTHON := ./venv/bin/python
PYTEST := ./venv/bin/pytest

guards:
	@echo "🛡️ Running Hive Guards..."
	@PYTHONPATH=. $(PYTHON) carapace/hive_guards/guard_brain.py
	@PYTHONPATH=. $(PYTHON) carapace/hive_guards/guard_mermaid.py
	@PYTHONPATH=. $(PYTHON) carapace/hive_guards/guard_gherkin_parity.py
	@PYTHONPATH=. $(PYTHON) carapace/hive_guards/guard_stigmergy_headers.py
	@PYTHONPATH=. $(PYTHON) carapace/hive_guards/guard_fractal_config.py
	@PYTHONPATH=. $(PYTHON) carapace/hive_guards/guard_hardcoded_values.py
	@PYTHONPATH=. $(PYTHON) venom/guard_reality.py
	@PYTHONPATH=. $(PYTHON) venom/guard_tool_integrity.py
	@echo "✨ All Guards Passed!"

test-all: guards
	@echo "🚀 Running ALL Smoke Tests..."
	@$(PYTHON) venom/smoke/test_01_ray.py
	@$(PYTHON) venom/smoke/test_02_temporal.py
	@$(PYTHON) venom/smoke/test_03_nats.py
	@$(PYTHON) venom/smoke/test_04_pydantic_instructor.py
	@$(PYTHON) venom/smoke/test_05_langgraph.py
	@$(PYTHON) venom/smoke/test_06_langsmith.py
	@$(PYTHON) venom/smoke/test_07_pgvector.py
	@$(PYTHON) venom/smoke/test_08_dspy.py
	@$(PYTHON) venom/smoke/test_09_gitops.py
	@$(PYTHON) venom/test_fractal_quorum.py
	@echo "✨ All Smoke Tests Passed!"

test-ray:
	@$(PYTHON) venom/smoke/test_01_ray.py

test-temporal:
	@$(PYTHON) venom/smoke/test_02_temporal.py

test-nats:
	@$(PYTHON) venom/smoke/test_03_nats.py

test-instructor:
	@$(PYTHON) venom/smoke/test_04_pydantic_instructor.py

test-langgraph:
	@$(PYTHON) venom/smoke/test_05_langgraph.py

test-langsmith:
	@$(PYTHON) venom/smoke/test_06_langsmith.py

test-pgvector:
	@$(PYTHON) venom/smoke/test_07_pgvector.py

test-dspy:
	@$(PYTHON) venom/smoke/test_08_dspy.py

test-gitops:
	@$(PYTHON) venom/smoke/test_09_gitops.py

# --- 🧬 Stem Cell Factory (Regeneration) ---

regenerate-agent:
	@echo "🦠 Regenerating Agent Role: $(role)..."
	@$(PYTHON) genesis.py --spawn-agent $(role)

# --- 🕸️ GraphRAG Operations ---

weave:
	@echo "🕷️ Weaving Knowledge Graph..."
	@$(PYTHON) body/digestion/weaver_ant.py

audit:
	@echo "🏛️ Convening Consensus Council..."
	@$(PYTHON) body/digestion/consensus_council.py

garden:
	@echo "🌿 Gardening (Pruning & Grafting)..."
	@$(PYTHON) body/digestion/graph_gardener.py

heal: weave garden audit
	@echo "✨ Hive Healed."

# --- 🛡️ GitOps ---

gitops:
	@echo "🛡️ Executing GitOps Protocol (Swarm Powered)..."
	@PYTHONPATH=. $(PYTHON) body/hands/infrastructure_gitops.py
	@echo "✅ Agent $(role) regenerated from Stem Cells."

clean-artifacts:
	@echo "🧹 Cleaning up ignored artifacts..."
	@git clean -fdX
	@echo "✅ Workspace Cleaned."

regenerate-organ:
	@echo "🫀 Regenerating Organ: $(name)..."
	@# TODO: Call genesis.py --regenerate-organ $(name)
	@echo "✅ Organ $(name) regenerated from Stem Cells."

phoenix-protocol:
	@echo "🔥 Initiating Phoenix Protocol (Hive Regeneration)..."
	@echo "⚠️  WARNING: This will reset the entire runtime environment."
	@# TODO: Call genesis.py --phoenix
	@echo "🦅 Hive Fleet Obsidian has risen from the ashes."

# --- 🦅 Swarm Operations ---

dashboard:
	@echo "🦅 Launching Swarm Dashboard..."
	@PYTHONPATH=. $(PYTHON) body/eyes/swarm_dashboard.py

run-swarm:
	@echo "🐜 Launching Obsidian Research Swarm..."
	@PYTHONPATH=. $(PYTHON) body/hands/research_swarm.py

research:
	@echo "🐜 Launching Research Mission: $(TOPIC)"
	@PYTHONPATH=. $(PYTHON) body/hands/research_swarm.py --mission "$(TOPIC)"

# --- 🕸️ The Three Webs ---

karmic-hunt:
	@echo "🕸️ Initiating Karmic Hunt for: $(intent)"
	@. .env && PYTHONPATH=. $(PYTHON) body/hands/obsidian_research_swarm.py --mission "KARMIC HUNT: $(intent). Use Cynefin to categorize the domain. Search for 'Exemplars' (Biomimicry, Open Source, Industry Standards). Synthesize a report with specific precedents."
