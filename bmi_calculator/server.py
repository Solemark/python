from flask import Flask, send_file, Response
from markupsafe import escape

from bmi import BMI

app = Flask(__name__)


@app.get("/")
def get_bmi_page() -> Response:
    return send_file("static/index.html")


@app.get("/script/<script>")
def get_script(script: str) -> Response:
    return send_file(f"static/{escape(script)}.js")


@app.get("/data/<height>/<weight>")
def get_bmi(height: float, weight: float) -> dict[str, str]:
    return {"rating": BMI(height, weight).get_rating()}
