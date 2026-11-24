from flask import Flask, request

app = Flask(__name__)

# Type whatever message you want your 16x16 RGB2 Panel to say!
MESSAGE = "HELLO FROM RENDER! "
index = 0

# Standard 6-bit binary values for Build Logic characters (1=a .. 26=z)
CHAR_NUM = {
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "1": 27,
    "2": 28,
    "3": 29,
    "4": 30,
    "5": 31,
    "6": 32,
    "7": 33,
    "8": 34,
    "9": 35,
    "0": 36,
    "!": 27,
    "?": 32,
    ".": 39,
}


@app.route("/endpoint", methods=["GET", "POST"])
def rgb2_talk():
    global index
    data = request.get_json(silent=True) or {}

    if str(data.get("value")) == "1":
        index = 0

    ch = MESSAGE[index]
    num = CHAR_NUM.get(ch.lower(), 0)

    # Convert number to 6 bits (b5 b4 b3 b2 b1 b0)
    b = format(num, "06b")

    # Map the 2x3 grid in column-major order (Left column top-to-bottom, Right column top-to-bottom)
    grid_bits = b[0] + b[2] + b[4] + b[1] + b[3] + b[5]

    is_shifted = (ch.isalpha() and ch.isupper()) or ch in ["!", "?"]
    shift_bit = "1" if is_shifted else "0"

    index = (index + 1) % len(MESSAGE)
    return shift_bit + grid_bits
