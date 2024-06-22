.PHONY: install
install:
	@echo "--- 🚀 Installing project dependencies for dev ---"
	poetry install --with dev

.PHONY: tests
tests:
	@echo "--- 🧪 Running tests ---"
	pytest tests/

.PHONY: lint
lint:
	@echo "--- 🧹 Linting code ---"
	poetry run pre-commit run --all-files
