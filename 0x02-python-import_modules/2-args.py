#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = 1
    if len(argv) == 2:
        print("{} argument".format(len(argv) - 1), end="")
    else:
        print("{} arguments".format(len(argv) - 1), end="")
    if len(argv) == 1:
        print(".")
    else:
        print(":")
        for i in argv[num:]:
            print("{}: {}".format(num, argv[num]))
            num += 1
