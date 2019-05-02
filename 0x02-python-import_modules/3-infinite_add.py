#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 3:
        print("{}".format(int(argv[1]) + int(argv[2])))
