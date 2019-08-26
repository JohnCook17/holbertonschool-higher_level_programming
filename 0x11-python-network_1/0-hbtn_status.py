#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as data:
        print_data = data.read()
        print("Body response:")
        print("\t- type: {}".format(type(print_data)))
        print("\t- content: {}".format(print_data))
        print("\t- utf8 content: {}".format(print_data.decode('utf-8')))
