def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("The size of height and weight lists are not the same.")
    if all(isinstance(i, (int, float)) for i in height + weight):
        return [w / (h ** 2) for h, w in zip(height, weight)]
    else:
        raise TypeError("Lists can only contain int or float")

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if all(isinstance(i, (int, float)) for i in bmi):
        return [True if i > limit else False for i in bmi]
    else:
        raise TypeError("The list can only contain int or float")

def main():

    print(give_bmi([2.71, 1.15], [165.3, 38.4]))


if __name__ == "__main__":
    main()
