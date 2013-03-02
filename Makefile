all: clean-pyc test

test:
	../venv/bin/python runtests.py

shell:
	../venv/bin/ipython

audit:
	../venv/bin/python audit

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

find-print:
	grep -r --include=*.py --exclude-dir=venv --exclude=fabfile* --exclude=tests.py --exclude-dir=tests --exclude-dir=commands 'print' ./

release:
	python setup.py sdist upload
	python setup.py bdist_wininst upload