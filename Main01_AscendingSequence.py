# Ascending sequence

# Stage 01 (main task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 16.10.2022


def ascending_sequence(number):
    while number > 0:
        if number % 10 <= number // 10 % 10:
            return False
        else:
            number = number // 10
    return True


def main():
    number = int(input("Input your number: "))

    result = ascending_sequence(number)
    if number < 0:
        msg = f"Enter a natural number."
    else:
        msg = (f"The digits of a number have an ascending sequence." if result
               else f"The digits of the number don't have an ascending sequence.")

    print(msg)


main()
