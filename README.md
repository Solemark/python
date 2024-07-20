# Python Meta

run tests with:

    pytest
    OR
    python -m unittest test_name.py
    OR
    python3 -m unittest discover -s . -p "*_test.py"

name is optional

run file with:

    python name.py
    OR
    python3 name.py
    
create a venv:
 
	python3 -m venv .venv

open venv with:

	. .venv/bin/activate

get dependencies with:

    pip3 install -r requirements.txt

run server with:

	flask --app <filename> run

run debug mode with:

	flask --app <filename> run --debug

filename does not need to include .py
