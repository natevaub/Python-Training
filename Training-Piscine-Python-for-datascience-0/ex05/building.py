import sys


def ispunch(char):
    punctuation = "!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    return char in punctuation


def main():
    if len(sys.argv) > 2:
        raise AssertionError("You should provide a single argument")
    elif len(sys.argv) == 1:
        user_input = input("Provide a string: ")
    else:
        user_input = sys.argv[1]

    result = {
        "character_count": 0,
        "upper_case_count": 0,
        "lower_case_count": 0,
        "punctuation_count": 0,
        "space_count": 0,
        "digit_count": 0,
    }

    for char in user_input:
        result["character_count"] += 1
        if char.isdigit():
            result["digit_count"] += 1
        elif char.islower():
            result["lower_case_count"] += 1
        elif char.isupper():
            result["upper_case_count"] += 1
        elif char.isspace():
            result["space_count"] += 1
        elif ispunch(char):
            result["punctuation_count"] += 1

    print(f"""The text contains {result["character_count"]} characters:
{result["upper_case_count"]} upper letters
{result["lower_case_count"]} lower letters
{result["punctuation_count"]} punctuation marks
{result["space_count"]} spaces
{result["digit_count"]} digits""")


if __name__ == "__main__":
    main()
