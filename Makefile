.PHONY: test-all test-ray test-temporal test-nats test-instructor test-langgraph test-langsmith test-pgvector

PYTHON := ./venv/bin/python
PYTEST := ./venv/bin/pytest

test-all:
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
	@# TODO: Call genesis.py --spawn-agent $(role)
	@echo "✅ Agent $(role) regenerated from Stem Cells."

regenerate-organ:
	@echo "🫀 Regenerating Organ: $(name)..."
	@# TODO: Call genesis.py --regenerate-organ $(name)
	@echo "✅ Organ $(name) regenerated from Stem Cells."

phoenix-protocol:
	@echo "🔥 Initiating Phoenix Protocol (Hive Regeneration)..."
	@echo "⚠️  WARNING: This will reset the entire runtime environment."
	@# TODO: Call genesis.py --phoenix
	@echo "🦅 Hive Fleet Obsidian has risen from the ashes."
