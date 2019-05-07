#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        firstchar = sentence[0]
    else:
        firstchar = None
    ret = length, firstchar
    return ret
