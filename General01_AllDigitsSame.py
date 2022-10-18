# All digits are the same

# Stage 01 (general task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 16.10.2022


def same_digits(number):
    if number <= 0:
        return -1
    while number > 9:
        if number % 10 != number // 10 % 10:
            return False
        number = number // 10
    return True


def main():
    number = int(input("Input your number: "))

    result = same_digits(number)
    if result == -1:
        msg = f"Enter a natural number."
    else:
        msg = (f"All digits of the number are the same." if result
               else f"All digits are not the same.")

    print(msg)


main()
