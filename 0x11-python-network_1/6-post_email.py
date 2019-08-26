#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    print_data = requests.post(argv[1], data={"email": argv[2]})
    print(print_data.text)
