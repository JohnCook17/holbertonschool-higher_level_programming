#!/usr/bin/python3

def ft(n):
    fact = 1
    for i in range(1,n + 1):
        fact = fact * i
    return fact

def pascal_triangle(n):
    res = []
    for i in range(n):
        row = []
        for e in range(i + 1):
            row.append(ft(i)/(ft(e)*ft(i-e)))
        res.append(row)
    return res
