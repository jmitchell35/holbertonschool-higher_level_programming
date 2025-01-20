#!/usr/bin/python3
def no_c(my_string):
    return "".join(char for char in my_string if char not in 'cC')
# iterating through string and += each char could also work
