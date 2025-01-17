#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    result = 0
    for i in range(0, argc - 1):
        result += int(argv[i + 1])
    print("{}".format(result))
