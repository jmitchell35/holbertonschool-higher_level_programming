#!/usr/bin/python3
"""
Module that adds all arguments to a list and saves them to a file.

This module combines functionality from save_to_json_file and
load_from_json_file to maintain a list of arguments in a JSON file.
Each time the script is run, it loads existing arguments, adds new ones
from command line, and saves the updated list back to the file.
"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    Add command line arguments to a list and save them to a JSON file.

    The function loads existing items from 'add_item.json' if it exists,
    adds any new command line arguments to the list, and saves the
    updated list back to the file. If the file doesn't exist, it starts
    with an empty list.

    Note:
        - The first argument (script name) is excluded
        - The file is created if it doesn't exist
    """
    filename = "add_item.json"

    try:
        args = load_from_json_file(filename)
    except FileNotFoundError:
        args = []

    args.extend(argv[1:])
    save_to_json_file(args, filename)


if __name__ == "__main__":
    add_item()
