#!/usr/bin/python3

def find_peak(list_of_integers):

    if not list_of_integers:
        return None
    print("starting")
    mid = len(list_of_integers)//2
    for _ in list_of_integers:
        mid_val = list_of_integers[mid]
        #print(mid_val)
        #print(mid)
        try:
            print("try worked")
            left = list_of_integers[mid - 1]
            right = list_of_integers[mid + 1]
        except:
            print("except")
            if right is None and left < mid_val:
                return mid_val
            if left is None and right < mid_val:
                return mid_val
        if left < mid_val and right < mid_val:
            print("peak found")
            return mid_val
        elif left and right:
            if left > mid_val:
                print("look left")
                mid_val = left
                mid -= 1
            if right > mid_val:
                print("look right")
                mid_val = right
                mid += 1
        elif mid_val == left and mid_val == right:
            return mid_val
        else:
            return None
