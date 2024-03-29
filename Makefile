install: ## Install dependencies
	poetry install

test-coverage: ## Prepare coverage report for Codeclimate
	poetry run pytest --cov=gendiff --cov-report xml

build: ## Build a package
	poetry build

package-install: ## Install built package
	python3 -m pip install --user dist/*.whl

package-reinstall: ## Reinstall built package
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff: ## Run main programm
	poetry run gendiff

lint: ## Run linter
	poetry run flake8 gendiff

test: ## Run tests
	poetry run pytest

help: ## This help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
