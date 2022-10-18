# Get max digit

# Stage 04 (main task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 18.10.2022

def get_max_digit(number):
    if number <= 0:
        return -1

    max_digit = 0

    while number > 0:
        digit = number % 10

        if digit == 9:
            max_digit = 9
            break

        if digit > max_digit:
            max_digit = digit
        number //= 10

    return max_digit


def main():
    number = int(input("Input your number: "))
    max_digit = get_max_digit(number)

    if max_digit == -1:
        msg = f"Enter a natural number."
    else:
        msg = f"In number {number} max digit {max_digit}"

    print(msg)


main()
