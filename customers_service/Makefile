all: test-unit test-integration test-e2e

test-unit:
	pipenv run pytest tests/unit --cov --cov-report lcov:lcov.info

test-e2e:
	pipenv run pytest tests/e2e

test-integration:
	pipenv run pytest tests/integration

format:
	pipenv run isort . --profile black
	pipenv run black src/ tests/

mypy:
	MYPYPATH=src pipenv run mypy src/ tests/

pylint:
	pipenv run pylint --ignore-paths '^src/build/.*$' src tests

check: mypy pylint
