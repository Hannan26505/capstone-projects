morse_code = {
    "A": ".-",    "B": "-...",  "C": "-.-.",
    "D": "-..",   "E": ".",     "F": "..-.",
    "G": "--.",   "H": "....",  "I": "..",
    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",
    "S": "...",   "T": "-",     "U": "..-",
    "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----."
}


def text_to_morse(text):
    result = []
    unsupported = []

    for character in text.upper():
        if character in morse_code:
            result.append(morse_code[character])
        elif character == " ":
            result.append("/")
        else:
            unsupported.append(character)

    return " ".join(result), unsupported

def main():
    text = input("Enter text to convert: ")

    if not text.strip():
        print("Please enter some text.")
    else:
        morse, unsupported = text_to_morse(text)

        print("Morse code:", morse)

    if unsupported:
        print("Unsupported characters:", set(unsupported))


if __name__ == "__main__":
    main()