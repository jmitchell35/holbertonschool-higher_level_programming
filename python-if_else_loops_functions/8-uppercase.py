#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # Checks if the chars lowercase
            # Python allows bounding ("surounding") a nb with inequations
            upper_str += chr(ord(char) - 32)  # Converts to uppercase, prints
        else:
            upper_str += char  # Print non-lowercase characters as is
    print("{}".format(upper_str))  # Prints a newline after the string
