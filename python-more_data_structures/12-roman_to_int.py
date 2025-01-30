#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    for char in roman_string:
        if char not in 'IVXLCDM':
            print("Le format du chiffre romain est incorrect")
            return -1

    roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L" : 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    }
    number = 0
    for i in range(len(roman_string)):
        if not roman_values[roman_string[i]]:
            return None
        else:
            if i + 1 in range(len(roman_string)) and roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
                number -= roman_values[roman_string[i]]
            else:
                number += roman_values[roman_string[i]]
    return number
