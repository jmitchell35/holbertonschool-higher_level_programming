#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        output = True
    except ValueError:
        output = False
    else:
        output = False
    
    return output
