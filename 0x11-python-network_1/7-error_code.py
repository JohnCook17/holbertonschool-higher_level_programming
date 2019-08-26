#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    site = requests.get(argv[1])
    if site.status_code >= 400:
        print("Error code: {}".format(site.status_code))
    else:
        print(site.text)
