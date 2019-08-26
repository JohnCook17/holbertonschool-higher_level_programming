#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    data = requests.get(argv[1])
    print(data.headers["X-Request-Id"])
