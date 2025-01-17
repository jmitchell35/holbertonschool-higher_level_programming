#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the hidden_4 module
    names = dir(hidden_4)

    # Filter and sort names (excluding names starting with "__")
    filtered_names = sorted(name for name in names if not name.startswith("__"))

    # Print each name on a new line
    for name in filtered_names:
        print(name)
