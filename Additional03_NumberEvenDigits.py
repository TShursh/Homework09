# Number of even digits in a number

# Stage 03 (additional task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 16.10.2022

def find_number_of_even_digit(number):
    if number <= 0:
        return -1
    count = 0
    while number > 0:
        if number % 10 % 2 == 0:
            count += 1
        number //= 10

    return count


def main():
    number = int(input("Input your number: "))

    result = find_number_of_even_digit(number)

    if result == -1:
        msg = f"Enter a natural number."
    else:
        msg = f"There are {result} even numbers in {number}."

    print(msg)


main()
