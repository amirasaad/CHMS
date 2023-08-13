all: test-unit test-integration test-e2e

test-unit:
	pipenv run pytest tests/unit --cov --cov-report lcov:lcov.info

test-unit-ci:
	pipenv run pytest tests/unit --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html
test-e2e:
	pipenv run pytest tests/e2e

test-integration:
	pipenv run pytest tests/integration

format:
	pipenv run isort . --profile black
	pipenv run black src/ tests/

mypy:
	MYPYPATH=src pipenv run mypy --ignore-missing-imports src/ tests/

pylint:
	pipenv run pylint --recursive=y customers_crud

check: mypy pylint
	pipenv run isort . --check-only --profile black
	pipenv run black --check src/ tests/
