.PHONY: test-all test-ray test-temporal test-nats test-instructor test-langgraph test-langsmith test-pgvector

PYTHON := ./venv/bin/python
PYTEST := ./venv/bin/pytest

test-all:
	@echo "🚀 Running ALL Smoke Tests..."
	@$(PYTHON) tests/smoke/test_01_ray.py
	@$(PYTHON) tests/smoke/test_02_temporal.py
	@$(PYTHON) tests/smoke/test_03_nats.py
	@$(PYTHON) tests/smoke/test_04_pydantic_instructor.py
	@$(PYTHON) tests/smoke/test_05_langgraph.py
	@$(PYTHON) tests/smoke/test_06_langsmith.py
	@$(PYTHON) tests/smoke/test_07_pgvector.py
	@$(PYTHON) tests/smoke/test_08_dspy.py
	@$(PYTHON) tests/smoke/test_09_gitops.py
	@echo "✨ All Smoke Tests Passed!"

test-ray:
	@$(PYTHON) tests/smoke/test_01_ray.py

test-temporal:
	@$(PYTHON) tests/smoke/test_02_temporal.py

test-nats:
	@$(PYTHON) tests/smoke/test_03_nats.py

test-instructor:
	@$(PYTHON) tests/smoke/test_04_pydantic_instructor.py

test-langgraph:
	@$(PYTHON) tests/smoke/test_05_langgraph.py

test-langsmith:
	@$(PYTHON) tests/smoke/test_06_langsmith.py

test-pgvector:
	@$(PYTHON) tests/smoke/test_07_pgvector.py

test-dspy:
	@$(PYTHON) tests/smoke/test_08_dspy.py

test-gitops:
	@$(PYTHON) tests/smoke/test_09_gitops.py
