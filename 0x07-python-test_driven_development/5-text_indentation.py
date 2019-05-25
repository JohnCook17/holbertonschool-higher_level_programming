#!/usr/bin/python3
""" Text indentation adds two newlines after ".", "?", ":"""""


def text_indentation(text):
    """Text indentation

    Args:
        text (str): text to indent

    Raise:
        TypeError

    """
    text = text.strip()
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev =""
    for alpha in text:
        if prev in [".", "?", ":"] and alpha is " ":
            continue
        prev = alpha
        print("{}".format(alpha), end="\n\n" if alpha in [".", "?", ":"] else"")
