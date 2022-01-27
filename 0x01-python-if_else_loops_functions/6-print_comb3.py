#!/usr/bin/python3
h = 0
while h < 9:
    j = h + 1
    while j < 10:
        print("{}".format(h), end="")
        if (h < 8 or j < 9):
            print("{},".format(j), end=" ")
        else:
            print("{}".format(j))
        j += 1
    h += 1
