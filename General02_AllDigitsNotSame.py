# All digits are not the same

# Stage 02 (general task)
# Subject theme: Python Basic Syntax. Conditional Statements
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 16.10.2022


def not_same_digits(number):
    while number > 0:
        last_digit = number % 10
        number2 = number
        while number2 >= 10:
            if last_digit == number2 // 10 % 10:
                return False
            number2 = number2 // 10
        number = number // 10
    return True


def main():
    number = int(input("Input your number: "))

    result = not_same_digits(number)
    if number < 0:
        msg = f"Enter a natural number."
    else:
        msg = (f"All digits of the number are different." if result
               else f"The number has the same numbers.")

    print(msg)


main()
