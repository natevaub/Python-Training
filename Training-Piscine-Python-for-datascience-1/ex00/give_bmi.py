import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    
    # How do I calculate my BMI?
    # You can calculate BMI yourself with these steps:

    # Multiply your weight in pounds by 703.
    # Divide that answer by your height in inches (there are 12 inches in 1 foot).
    # Divide that answer by your height in inches again.
    # For example, a person who weighs 180 lbs. and is 5 feet and 5 inches tall (65 inches total) would calculate their BMI in the following way:

    # 180 x 703 = 126,540
    # 126,540 / 65 = 1,946.769
    # 1,946.769 / 65 = 29.95
    # Their BMI would be 29.9.

    a = np.array(height)
    b = np.array(weight)
    # Check if the lists are the same size
    if len(a) != len(b):
        raise ValueError("The lists must be the same size.")
    # Check if the lists contain only int or float
    if not all(isinstance(i, (int, float)) for i in a) or not all(isinstance(i, (int, float)) for i in b):
        raise ValueError("The lists must contain only int or float.")
    # Check if the lists are not empty
    if len(a) == 0 or len(b) == 0:
        raise ValueError("The lists must not be empty.")
    # Check if the lists contain only positive values
    if any(i <= 0 for i in a) or any(i <= 0 for i in b):
        raise ValueError("The lists must contain only positive values.")

    # Convert height from feet to inches
    step1 = b * 703
    print(step1)

    return step1.ravel()



    
# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    
    # pass

# Your function, give_bmi, take 2 lists of integers or floats in input and returns a list
# of BMI values.
# Your function, apply_limit, accepts a list of integers or floats and an integer representing
# a limit as parameters. It returns a list of booleans (True if above the limit).
# You have to handle error cases if the lists are not the same size, are not int or float...
# The prototype of functions is:
# def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
# #your code here
# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
# #your code here
# Your tester.py:
# from give_bmi import give_bmi, apply_limit
# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
# Expected output:
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class 'list'>
# [False, True]
# $>
# 4

def main():
    give_bmi([2.71, 1.15], [165.3, 38.4])

    
    

if __name__ == "__main__":
    main()
