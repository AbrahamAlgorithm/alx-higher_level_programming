#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        print(number % 10, end="")
        return (number % 10)
    elif number == 0:
        print(0, end="")
        return (0)
    else:
        print(-number % 10, end="")
        return (-number % 10)
