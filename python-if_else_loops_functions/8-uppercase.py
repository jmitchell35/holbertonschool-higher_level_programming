#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Checks if the character is lowercase
        # Python allows bounding ("surounding") a number in such inequation
            print(chr(ord(char) - 32), end="") # Converts to uppercase, prints
        else:
            print(char, end="")  # Print non-lowercase characters as is
    print()  # Prints a newline after the string
