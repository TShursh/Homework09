# Bank deposit

# Stage 03 (main task)
# Subject theme: Python Basic Syntax. While Loop Statement. Iteration Algorithms
# Version: 2.0
# Author: Irtikeeva Tatiana
# Company: IT Academy Step
# Date: 17.10.2022

def bank_deposit(percent):
    if not 0 < percent < 25:
        return -1, -1
    deposit_sum = 1000
    month = 0
    while deposit_sum < 2000:
        deposit_sum += deposit_sum / 100 * percent / 12
        # Banking always uses annual interest, so we divide by 12.
        month += 1
    return month, deposit_sum


def main():
    percent = int(input("Input deposit percent: "))

    month, deposit_sum = bank_deposit(percent)

    if month == -1:
        msg = f"Please, input a percent from 1 to 24."
    else:
        msg = f"After {month} months you will have accumulated an amount of {round(deposit_sum, 2)}"
    print(msg)


main()
