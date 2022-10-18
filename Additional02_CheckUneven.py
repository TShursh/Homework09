# Check digit uneven

# Stage 02 (additional task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 18.10.2022


def check_digit_uneven(number):
    if number <= 0:
        return -1
    while number > 0:
        if number % 10 % 2 == 0:
            return False
        number //= 10
    return True


def main():
    number = int(input("Input your number: "))

    result = check_digit_uneven(number)
    if result == -1:
        msg = f"Enter a natural number."
    else:
        msg = (f"All digits of the number are uneven." if result
               else f"All digits are not uneven.")

    print(msg)


main()
