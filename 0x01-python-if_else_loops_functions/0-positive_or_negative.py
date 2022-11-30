#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(f"{number} is", end=" ")
if (number is 0):
    print(f"zero")
elif (number < 0):
    print(f"negative")
else:
    print(f"positive")
