#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_value = my_list[0]
    for nb in my_list:
        if nb > max_value:
            max_value = nb

    return max_value
