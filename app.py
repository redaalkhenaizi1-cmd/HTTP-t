from flask import Flask, request

app = Flask(__name__)

# 8-pixel-tall columns spelling "HI!" with blank spacer columns
FRAMES = [
    "11111111",  # H left bar
    "00011000",  # H middle bar
    "11111111",  # H right bar
    "00000000",  # space
    "10000001",  # I top & bottom
    "11111111",  # I center bar
    "10000001",  # I top & bottom
    "00000000",  # space
    "11111011",  # ! exclamation mark
    "00000000",  # space
]
step = 0


@app.route("/endpoint", methods=["GET", "POST"])
def panel_talk():
    global step
    data = request.get_json(silent=True) or {}

    # Turn your input switch ON ("1") and trigger POST to restart from the beginning
    if str(data.get("value")) == "1":
        step = 0

    column = FRAMES[step]
    step = (step + 1) % len(FRAMES)
    return column
