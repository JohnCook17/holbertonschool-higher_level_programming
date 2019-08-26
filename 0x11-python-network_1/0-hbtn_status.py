#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as data:
        print_data = data.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(print_data))
        print("\t- utf8 content: {}".format(print_data.decode('utf-8')))
