#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dg = abs(number) % 10
if number < 0:
    last_dg = -last_dg
print(f"Last digit of {number} is {last_dg}", end=" ")
if last_dg > 5:
    print(f"and is greater than 5")
elif last_dg == 0:
    print(f"and is 0")
elif last_dg < 6 and last_dg != 0:
    print(f"and is less than 6 and not 0")
