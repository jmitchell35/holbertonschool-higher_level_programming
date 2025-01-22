#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_nb = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_nb += 1

    except IndexError:
        pass

    return printed_nb
