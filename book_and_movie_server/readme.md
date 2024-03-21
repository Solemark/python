create a venv:
 
	python3 -m venv .venv

open venv with:

    . .venv/bin/activate

get dependencies with:

    pip3 install -r requirements.txt

run server(s) with:

    flask --app book_server run -p 8001
    flask --app movie_server run -p 8002
    flask --app server_coordinator run -p 8003
    python3 order_client.py

run debug mode with:

    flask --app <filename> run --debug

filename does not need to include .py
