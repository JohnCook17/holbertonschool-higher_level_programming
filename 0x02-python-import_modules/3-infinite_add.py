#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = 1
    sums = 0
    for i in argv[num:]:
        sums += int(argv[num])
        num += 1
    print("{}".format(sums))
