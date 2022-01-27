#!/usr/bin/python3
def uppercase(str):
    j = len(str)
    for i in range(j):
        to_change = ord(str[i])
        if 97 <= to_change <= 122:
            to_change = to_change - 32
        print("{}".format(chr(to_change)), end="")
    print()
