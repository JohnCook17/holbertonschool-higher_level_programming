#!/usr/bin/python3
import requests

if __name__ == "__main__":
    data = requests.get("https://intranet.hbtn.io/status")
    print_data = data.text
    print("Body response:")
    print("\t- type: {}".format(type(print_data)))
    print("\t- content: {}".format(print_data))
