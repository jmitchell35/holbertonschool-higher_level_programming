#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print(f"{i:01}{j:01}", end=", " if i < 8 else "\n")
# i iterates through all digits
# j is always greater, avoiding repetition
# format string ensures two-digit number
# if/else ensures new line is printed only after last combination
