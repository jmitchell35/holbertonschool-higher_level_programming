#!/usr/bin/env python3
def islower(c):
    if 97 <= ord(c) <= 122:  # easy condition, see inequation
        return True  # watch for capital letter
    else:
        return False
# output is handled inside testing main function
# e.g.: prnt("a is {}".format("lower" if islower("a") else "upper"))
