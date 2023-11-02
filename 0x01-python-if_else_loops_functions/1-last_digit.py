#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = 0
if number < 0:
    n = -(-number % 10)
else:
    n = number % 10
print("Last digit of {} is {} and is ".format(number, n), end="")
if n > 5:
    print("greater than 5")
elif n == 0:
    print('0')
else:
    print('less than 6 and not 0')
