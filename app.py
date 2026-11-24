from flask import Flask, request

app = Flask(__name__)

# Type whatever message you want your 16x16 RGB2 Panel to say!
MESSAGE = "HELLO FROM RENDER! "
index = 0

# 7-bit codes for the RGB2 Panel's "Characters" pins (SHIFT + 6 bits)
CHAR_MAP = {
    " ": "0000000",
    "a": "0000001",
    "b": "0000010",
    "c": "0000011",
    "d": "0000100",
    "e": "0000101",
    "f": "0000110",
    "g": "0000111",
    "h": "0001000",
    "i": "0001001",
    "j": "0001010",
    "k": "0001011",
    "l": "0001100",
    "m": "0001101",
    "n": "0001110",
    "o": "0001111",
    "p": "0010000",
    "q": "0010001",
    "r": "0010010",
    "s": "0010011",
    "t": "0010100",
    "u": "0010101",
    "v": "0010110",
    "w": "0010111",
    "x": "0011000",
    "y": "0011001",
    "z": "0011010",
    "1": "0011011",
    "2": "0011100",
    "3": "0011101",
    "4": "0011110",
    "5": "0011111",
    "6": "0100000",
    "7": "0100001",
    "8": "0100010",
    "9": "0100011",
    "0": "0100100",
    "!": "1011011",
    "?": "1100000",
    ".": "0100111",
}


@app.route("/endpoint", methods=["GET", "POST"])
def rgb2_talk():
    global index
    data = request.get_json(silent=True) or {}

    # Flip your input switch ON ("1") and trigger POST to restart from the beginning
    if str(data.get("value")) == "1":
        index = 0

    ch = MESSAGE[index]
    code = CHAR_MAP.get(ch.lower(), "0000000")

    # If the letter is UPPERCASE, turn the first bit (SHIFT) to "1"
    if ch.isalpha() and ch.isupper():
        code = "1" + code[1:]

    index = (index + 1) % len(MESSAGE)
    return code[::-1]
