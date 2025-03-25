# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>
# Running your function alone does nothing.
# Expected output:
# $>python NULL_not_found.py | cat -e

def NULL_not_found(object: any) -> int:

    var_nothing = None
    var_nan = float("NaN")
    var_zero = 0
    var_empty = ''
    var_bool = False

    if type(object) is type(var_nothing):
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is type(var_nan):
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is type(var_zero):
        print(f"Zero: {object} {type(object)}")
    elif type(object) is type(var_empty):
        print(f"Empty: {object} {type(object)}")
    elif type(object) is type(var_bool):
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0