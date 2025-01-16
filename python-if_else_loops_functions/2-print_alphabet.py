#!/usr/bin/python3
print("".join(f"{i:c}" for i in range(97, 123)), end="")
# using f-string formatting
# old formatting from python 2.6 also possible :
# print("".join("{:c}".format(i) for i in range(97, 123)), end="")
