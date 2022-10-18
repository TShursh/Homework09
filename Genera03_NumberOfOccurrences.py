# Number of occurrences of a digit in a number

# Stage 03 (general task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 16.10.2022

def number_of_occurrences(search_number, number):
    count = 0
    while number > 0:
        if search_number == number % 10:
            count += 1
        number = number // 10

    return count


def main():
    search_number = int(input("Input your search number: "))
    number = int(input("Input your number: "))

    result = number_of_occurrences(search_number, number)

    if number <= 0:
        msg = f"Enter a natural number."
    else:
        msg = f"The number {search_number} occurs {result} times in the number {number}."

    print(msg)


main()
