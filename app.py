from flask import Flask, request

app = Flask(__name__)

# Tests each of the 7 output pins one by one!
PINS = [
    "1000000",  # Pin 1
    "0100000",  # Pin 2
    "0010000",  # Pin 3
    "0001000",  # Pin 4
    "0000100",  # Pin 5
    "0000010",  # Pin 6
    "0000001",  # Pin 7
]
step = 0


@app.route("/endpoint", methods=["GET", "POST"])
def test_pins():
    global step
    out = PINS[step]
    step = (step + 1) % len(PINS)
    return out
