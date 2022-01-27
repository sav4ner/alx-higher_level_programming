#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    base = len(sys.argv) - 1
    if base == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(base))
    for j in range(base):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
