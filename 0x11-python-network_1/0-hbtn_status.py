#!/usr/bin/python3
if __name__ == "__main__":
    from urllib import request
    with request.urlopen("https://intranet.hbtn.io/status") as data:
        print_data = data.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(print_data))
        print("\t- utf8 content: {}".format(print_data.decode('utf8')))
