#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = []
    for element in my_list:
        if element == search:
            my_new_list.append(replace)
        else:
            my_new_list.append(element)
    return my_new_list
