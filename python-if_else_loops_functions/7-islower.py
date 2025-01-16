#!/usr/bin/env python3
def islower(c):
    if ord(c) >=97 and ord(c) <= 122: # easy condition
        return True # watch for capital letter
    else:
        return False
# output is handled inside testing main function
# e.g.: print("a is {}".format("lower" if islower("a") else "upper"))
