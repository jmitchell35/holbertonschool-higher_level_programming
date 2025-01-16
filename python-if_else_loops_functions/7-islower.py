#!/usr/bin/python3
def islower(c):
    if 97 <= ord(c) <= 122:  # easy condition, notice inequation
        return True  # watch for capital letter
    else:
        return False
