#!/usr/bin/python3
print("".join(f"{i:c}" for i in range(97, 123) if i not in (101, 113)), end="")
# also f-string formatting
# alternatively :
# print("".join("{:c}".format(i) for i in range(97, 123)
#  if i not in (101, 113)), end="")
