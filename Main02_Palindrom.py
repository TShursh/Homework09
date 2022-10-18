# Palindrom

# Stage 02 (main task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 17.10.2022

def palindrom(number):
    if number <= 0:
        return -1
    ls = []
    while number > 0:
        last_digit = number % 10
        ls.append(last_digit)
        number = number // 10

    while len(ls) != 0:
        if ls[0] != ls[len(ls) - 1]:
            return False
        ls = ls[1:len(ls) - 1]

    return True


def main():
    number = int(input("Input your number: "))

    result = palindrom(number)

    if result == -1:
        msg = f"Enter a natural number."
    else:
        msg = (f"Your number is a palindrome." if result
               else f"Your number is not a palindrome.")

    print(msg)


main()
