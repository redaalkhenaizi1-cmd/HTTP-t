from flask import Flask, request

app = Flask(__name__)

# Type whatever message you want your 16x16 RGB2 Panel to say!
MESSAGE = "HELLO FROM RENDER! "
index = 0

# Exact 6-bit character codes for Build Logic's RGB2 Panel
CHAR_MAP = {
    " ": "000000",
    "a": "000001",
    "b": "000010",
    "c": "000011",
    "d": "000100",
    "e": "000101",
    "f": "000110",
    "g": "000111",
    "h": "001000",
    "i": "001001",
    "j": "001010",
    "k": "001011",
    "l": "001100",
    "m": "001101",
    "n": "001110",
    "o": "001111",
    "p": "010000",
    "q": "010001",
    "r": "010010",
    "s": "010011",
    "t": "010100",
    "u": "010101",
    "v": "010110",
    "w": "010111",
    "x": "011000",
    "y": "011001",
    "z": "011010",
    "1": "011011",
    "2": "011100",
    "3": "011101",
    "4": "011110",
    "5": "011111",
    "6": "100000",
    "7": "100001",
    "8": "100010",
    "9": "100011",
    "0": "100100",
    "!": "011011",
    "?": "100000",
    ".": "100111",
}


@app.route("/endpoint", methods=["GET", "POST"])
def rgb2_talk():
    global index
    data = request.get_json(silent=True) or {}

    if str(data.get("value")) == "1":
        index = 0

    ch = MESSAGE[index]
    bits = CHAR_MAP.get(ch.lower(), "000000")

    # SHIFT bit goes on Pin 1 ("1" for uppercase or !/?, "0" for lowercase)
    is_shifted = (ch.isalpha() and ch.isupper()) or ch in ["!", "?"]
    shift_bit = "1" if is_shifted else "0"

    index = (index + 1) % len(MESSAGE)

    # Keep SHIFT on Pin 1 and reverse the 6 character bits to match your wires
    return shift_bit + bits[::-1]
