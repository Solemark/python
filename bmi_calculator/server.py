from flask import Flask, send_file, Response
from markupsafe import escape

from bmi import BMI

app = Flask(__name__)


@app.get("/")
def get_bmi_page() -> Response:
    """Return the index page"""
    return send_file("static/index.html")


@app.get("/script/<script>")
def get_script(script: str) -> Response:
    """Return the js file"""
    return send_file(f"static/{escape(script)}.js")


@app.get("/data/<height>/<weight>")
def get_bmi(height: float, weight: float) -> dict[str, str]:
    """Get the BMI rating"""
    return {"rating": BMI(height, weight).get_rating()}
