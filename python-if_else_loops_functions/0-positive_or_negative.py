#!/usr/bin/python3
import random

number = random.randint(-10, 10)  # This line generates a random signed number

print(number, end=", ")
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
