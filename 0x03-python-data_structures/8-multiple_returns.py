#!/usr/bin/python3
"""
A function that returns a tuple with the length of a string
and its first character
"""


def multiple_returns(sentence):
    if (sentence is None or len(sentence) == 0):
        s_len = 0
        f_char = None
    else:
        s_len = len(sentence)
        f_char = sentence[0]
    return (s_len, f_char)
