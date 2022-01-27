#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasdgt = abs(number) % 10
ms = "Last digit of "
if number < 0:
    lasdgt = -lasdgt
print("{}{} is {} and is ".format(ms, number, lasdgt), end="")
if lasdgt > 5:
    print("greater than 5")
elif lasdgt == 0:
    print("0")
else:
    print("less than 6 and not 0")
