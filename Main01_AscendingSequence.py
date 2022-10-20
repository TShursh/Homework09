# Ascending sequence

# Stage 01 (main task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 16.10.2022


def ascending_sequence(number):
    while number > 10:
        if number % 10 <= number // 10 % 10:
            return False
        number //= 10
    return True


def descending_sequence(number):
    while number > 10:
        if number % 10 >= number // 10 % 10:
            return False
        number //= 10
    return True


def main():
    number = int(input("Input your number: "))

    if number < 0:
        msg = f"Enter a natural number."
    elif ascending_sequence(number):
        msg = f"The digits of a number have an ascending sequence."
    elif descending_sequence(number):
        msg = f"The digits of a number have an descending sequence."
    else:
        msg = f"The numbers do not form a sequence."

    print(msg)


main()
