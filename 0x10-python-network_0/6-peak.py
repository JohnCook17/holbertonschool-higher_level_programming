#!/usr/bin/python3


def find_peak(list_of_integers):

    if not list_of_integers:
        return None
    mid = len(list_of_integers)//2
    for _ in list_of_integers:
        mid_val = list_of_integers[mid]
        try:
            left = list_of_integers[mid - 1]
            right = list_of_integers[mid + 1]
        except:
            if right is None and left < mid_val:
                return mid_val
            if left is None and right < mid_val:
                return mid_val
        if left < mid_val and right < mid_val:
            return mid_val
        elif left and right:
            if left > mid_val:
                mid_val = left
                mid -= 1
            if right > mid_val:
                mid_val = right
                mid += 1
        elif mid_val == left and mid_val == right:
            return mid_val
        else:
            return None
