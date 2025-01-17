#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    print(
            "{} {}{}".format(
                argc,
                "argument" if argc == 1 else "arguments",
                "." if argc == 0 else ":"
                )
            )
    for i in range(0, argc):
        print("{}: {}".format(i + 1, argv[i + 1]))
