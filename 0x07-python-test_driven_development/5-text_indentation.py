#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev =""
    for alpha in text:
        if prev in [".", "?", ":"] and alpha is " ":
            continue
        prev = alpha
        print("{}".format(alpha), end="\n\n" if alpha in [".", "?", ":"] else"")
