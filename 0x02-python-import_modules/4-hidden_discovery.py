#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list1 = dir(hidden_4)
    num = 0
    for i in list1[num:]:
        if "__" not in list1[num]:
            print("{}".format(list1[num]))
        num += 1
