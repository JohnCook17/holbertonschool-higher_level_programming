#!/usr/bin/python3
""" sorts a list """


class MyList(list):
    """sorts a list

    """
    def print_sorted(self):
        sorted_list = self
        sorted_list.sort()
        print("{}".format(sorted_list))
