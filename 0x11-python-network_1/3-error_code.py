#!/usr/bin/python3
import urllib.request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as data:
            print_data = data.read()
            print(print_data.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
