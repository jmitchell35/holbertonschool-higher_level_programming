#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str) == False:
        return 0
    decimal = 0
    for i in range(len(roman_string)):
        if roman_string[i] == 'I':
            if (i + 1 in range(len(roman_string)) and 
                roman_string[i + 1] in 'VX'):
                decimal -= 1
            else:
                decimal += 1

        if roman_string[i] == 'V':
            decimal += 5

        if roman_string[i] == 'X':
            if (i + 1 in range(len(roman_string)) and
                roman_string[i + 1] in 'LC'):
                decimal -= 10
            else:
                decimal += 10

        if roman_string[i] == 'L':
            decimal += 50
        
        if roman_string[i] == 'D':
            decimal += 500

        if roman_string[i] == 'C':
            if (i + 1 in range(len(roman_string)) and
                roman_string[i + 1] in 'DM'):
                decimal -= 100
            else:
                decimal += 100

        if roman_string[i] == 'M':
            decimal += 1000

    return decimal
