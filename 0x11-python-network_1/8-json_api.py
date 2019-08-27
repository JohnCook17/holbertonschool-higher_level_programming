#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        letter = ""
    else:
        letter = {"q": argv[1]}
    my_data = requests.post("http://0.0.0.0:5000/search_user", letter)
    if len(argv) != 2:
        print("No result")
    else:
        try:
            my_data.json()
            print("[{}] {}".format(my_data.json()["id"], my_data.json()["name"]))
        except:
            print("Not a valid JSON")
