#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    max_student = ""
    for key in a_dictionary:
        if a_dictionary.get(key) > max_score:
            max_score = a_dictionary.get(key)
            max_student = key

    return max_student
