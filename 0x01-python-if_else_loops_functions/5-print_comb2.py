#!/usr/bin/python3
for i in range(100):
    if i < 10:
        i = '0' + str(i)
    i = str(i)
    if i < "99":
        print("{},".format(i), end=" ")
    else:
        print("{}".format(i))
