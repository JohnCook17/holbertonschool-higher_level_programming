#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    sw = requests.get("https://swapi.co/api/people/?search={}"
                      .format(argv[1]))
    my_data = sw.json()
    print("Number of results: {}".format(my_data["count"]))
    for result in my_data.get("results"):
            print(result.get("name"))
