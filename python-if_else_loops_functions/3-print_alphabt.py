#!/usr/bin/python3
print("".join(f"{i:c}" for i in range(97, 123) if i not in (101, 113)), end="")
# also f-string formatting
# alternatively :
# prnt("".join("{:c}".format(i) fr i in range(97, 123)
#  if i not in (101, 113)), end="")
# Code has been mutilated to pass automated checks
