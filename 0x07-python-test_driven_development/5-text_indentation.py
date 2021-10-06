#!/usr/bin/python3
"""
Function that print a square
Returns nothing
works with character #
"""


def text_indentation(text):
    """Function print two new lines after this character: .,? and :
    checking if text is a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = 0
    text = text.strip()
    for i in range(len(text)):
        if a == 1 and text[i] == " ":
            a = 0
        else:
            if text[i] == " " and (text[i - 1]) == " ":
                ()
            else:
                print("{}".format(text[i]), end="")
        if text[i] is "?" or text[i] is "." or text[i] is ":":
            a = 1
            print("\n")
