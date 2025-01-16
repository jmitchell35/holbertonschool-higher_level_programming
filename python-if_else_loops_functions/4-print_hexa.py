#!/usr/bin/python3
print("".join(f"{i} = 0x{i:x}\n" for i in range(99)), end="")
# still using f-strings formatting
# format specifiers : b for binaries, x for hex, #x to add 0x prefix...
