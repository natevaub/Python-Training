import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    # Error handling
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    new_array = np.array(family)[start:end].tolist()
    print(f"My new shape is : ({len(new_array)}, {len(new_array[0])})")

    return new_array


def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
