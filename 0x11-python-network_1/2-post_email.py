#!/usr/bin/python3
from urllib import request, parse
from sys import argv
if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as result:
        print(result.read().decode("utf-8"))
