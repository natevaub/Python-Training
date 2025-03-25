import sys

if len(sys.argv) < 2:
    exit()
elif len(sys.argv) > 2:
    raise AssertionError("More than one argument is provided")

try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError("Argument is not a number")

if number % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")