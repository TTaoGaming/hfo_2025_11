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

micro-swarm:
	@echo "🔬 Testing Micro-Swarm Concurrency (8 Agents)..."
	@$(PYTHON) venom/test_swarm_concurrency.py

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

# --- 🧠 Memory & Ingestion ---
ingest-unified:
	@echo "📥 Running Unified Ingestion (Frameworks + Brain)..."
	@PYTHONPATH=. $(PYTHON) scripts/unified_ingest.py

ingest-horizon:
	@echo "📥 Ingesting Obsidian Horizon..."
	@PYTHONPATH=. $(PYTHON) scripts/ingest_obsidian_horizon.py

ingest-prey:
	@echo "📥 Ingesting 1-1-1-1 PREY Loop Intent..."
	@KMP_DUPLICATE_LIB_OK=TRUE OMP_NUM_THREADS=1 PYTHONPATH=. $(PYTHON) buds/hfo_gem_gen_55/scripts/ingest_prey_loop.py

memory-query:
	@echo "🧠 Querying Swarmlord Memory..."
	@read -p "Enter query: " query; \
	PYTHONPATH=. $(PYTHON) -c "import asyncio; from body.hands.swarmlord import SwarmlordAgent; \
	async def q(): \
		a = SwarmlordAgent(); \
		await a.initialize(); \
		print(await a.chat('$$query')); \
		await a.close(); \
	asyncio.run(q())"


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

# --- ⚡ Stigmergy System (Gen 55) ---

stigmergy-setup:
	@echo "⚡ Setting up Stigmergy Infrastructure (NATS + LanceDB)..."
	@PYTHONPATH=. $(PYTHON) buds/hfo_gem_gen_55/scripts/setup_stigmergy.py

stigmergy-assimilator:
	@echo "⚡ Starting Stigmergy Assimilator (Hot -> Cold)..."
	@PYTHONPATH=. $(PYTHON) buds/hfo_gem_gen_55/scripts/run_assimilator.py

stigmergy-test:
	@echo "⚡ Testing Stigmergy System (8 Pillars)..."
	@PYTHONPATH=. $(PYTHON) buds/hfo_gem_gen_55/venom/tests/test_stigmergy_system.py

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
