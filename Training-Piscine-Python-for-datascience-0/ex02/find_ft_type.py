
def all_thing_is_obj(object: any) -> int:

    list_type: list = []
    list_tuple: tuple = ()
    list_set: set = set()
    list_dict: dict = {}

    if type(object) is type(list_type):
        print(f"List: {type(object)}")
    elif type(object) is type(list_tuple):
        print(f"Tuple: {type(object)}")
    elif type(object) is type(list_set):
        print(f"Set: {type(object)}")
    elif type(object) is type(list_dict):
        print(f"List: {type(object)}")
    elif type(object) is type(10):
        print("Type not found")
    elif type(object) is type(""):
        print(f"{object} is in the kitchen")

    return 42


