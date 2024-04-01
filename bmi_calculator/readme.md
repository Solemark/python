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
