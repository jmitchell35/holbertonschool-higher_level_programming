#!/usr/bin/python3
print("".join("{i} = 0x{i:x}\n".format(i=i) for i in range(99)), end="")
# f-strings formatting :
# prnt("".join(f"{i} = 0x{i:x}\n" fr i in range(99)), end="")
# format specifiers : b fr binaries, x fr hex, #x to add 0x prefix...
