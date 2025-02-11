#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as f:
        nb_of_char = f.write(text)
    
    return (nb_of_char)