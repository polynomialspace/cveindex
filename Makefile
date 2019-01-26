all:
	touch data/
	python3 main.py -s debian -s redhat -fi
clean:
	rm -rf data/* cve.db __pycache__/ ./*/__pycache__ ./*/*/__pycache__
