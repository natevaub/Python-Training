import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "---.- ",
}

def get_value(char):
    if char.upper() in NESTED_MORSE:
        return NESTED_MORSE[char.upper()]
    return None
        


def custom_isalnum(arg):
    for x in arg:
        if not (
            (ord(x) >= 48 and ord(x) <= 57)
            or (ord(x) >= 65 and ord(x) <= 90)
            or (ord(x) >= 97 and ord(x) <= 122)
            or (ord(x) == 32)
        ):
            return False

    return True


def main():
    if len(sys.argv) != 2:
        raise AssertionError("You should provide one argument")
    elif not custom_isalnum(sys.argv[1]):
        raise AssertionError("Unsupported characters")

    print(
        f"""ARG: {sys.argv[1]} --- isspace = {sys.argv[1].isspace()}
--- isalnum = {sys.argv[1].isalnum()}
--- alnum or space {custom_isalnum(sys.argv[1])}"""
    )

    res = ""

    for x in sys.argv[1]:
        res += get_value(x)

    print(f"{res}")


if __name__ == "__main__":
    main()
