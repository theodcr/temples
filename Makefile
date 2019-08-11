format:
	isort -rc temples/
	isort -rc tests/
	black temples/
	black tests/

test:
	env TEMPLE_CONFIG=./tests/linreg/config python tests/linreg/run_linreg.py
