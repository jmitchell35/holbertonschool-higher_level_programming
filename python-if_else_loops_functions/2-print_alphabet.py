#!/usr/bin/python3
print("".join("{:c}".format(i) for i in range(97, 123)), end="")
# using f-string formatting
# print("".join(f"{i:c}" for i in range(97, 123)), end="")
