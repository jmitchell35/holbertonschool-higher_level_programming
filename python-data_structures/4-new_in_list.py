#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        for i in range(len(my_list)):
            my_new_list.append(my_list[i])
        my_new_list[idx] = element
    return my_new_list
