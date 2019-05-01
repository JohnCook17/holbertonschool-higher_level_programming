#!/usr/bin/python3
def islower(c):
    for i in c:
        for alpha in range(ord('a'), ord('z')+1):
            if ord(i) == alpha:
                return True
    return False
