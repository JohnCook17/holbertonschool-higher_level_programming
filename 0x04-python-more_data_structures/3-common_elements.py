#!/usr/bin/python3
def common_elements(set_1, set_2):
#    return [list(map(lambda x, y: x if x == y else None, set_1, set_2))]
    new_set = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                new_set.add(j)
    return new_set
