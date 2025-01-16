#!/usr/bin/python3
def fizzbuzz():
    for nb in range(1, 101):
        if not nb % 3 and not nb % 5:
            print("FizzBuzz", end=" ")
        elif not nb % 3:
            print("Fizz", end=" ")
        elif not nb % 5:
            print("Buzz", end=" ")
        else:
            print(nb, end=" ")
