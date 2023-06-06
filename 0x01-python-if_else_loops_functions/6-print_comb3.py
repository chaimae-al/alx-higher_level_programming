#!/usr/bin/python3

for ndig1 in range(0, 10):
    for ndig2 in range(ndig1 + 1, 10):
        if ndig1 == 8 and ndig2 == 9:
            print("{}{}".format(ndig1, ndig2))
        else:
            print("{}{}".format(ndig1, ndig2), end=", ")
