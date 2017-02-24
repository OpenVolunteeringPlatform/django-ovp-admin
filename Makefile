test:
	@python ovp_admin/tests/runtests.py

lint:
	@pylint ovp_admin

clean-pycache:
	@rm -r **/__pycache__

clean: clean-pycache

.PHONY: clean


