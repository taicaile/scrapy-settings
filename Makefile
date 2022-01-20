install:
	pip uninstall scrapy-settings -y
	python setup.py install

test:
	python tests/test.py

clear:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
