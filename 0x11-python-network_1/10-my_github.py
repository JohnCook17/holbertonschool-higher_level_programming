#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    my_data = requests.get("https://api.github.com/user",
                           auth=(argv[1], argv[2]))
    print(my_data.json().get("id"))
