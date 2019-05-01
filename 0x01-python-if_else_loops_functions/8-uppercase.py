#!/usr/bin/python3
def uppercase(str):
    for i in str:
        for alpha in range(ord('a'), ord('z')+1):
            if ord(i) == alpha:
                i = chr(ord(i) - 32)
                continue
        print("{}".format(i), end="")
    print("")
