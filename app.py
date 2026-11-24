from flask import Flask, request

app = Flask(__name__)


@app.route("/endpoint", methods=["GET", "POST"])
def home():
    data = request.get_json(silent=True) or {}
    if str(data.get("value")) == "1":
        return "11111111"
    return "10101010"
