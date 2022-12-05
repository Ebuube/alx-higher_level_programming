#!/usr/bin/python3
"""
A program that prints all the names defined by the compiled module
hidden_4.pyc (downloaded locally)
"""


if __name__ == "__main__":
    import hidden_4.pyc as hidden_4
    for name_def in hidden_4
    if name_def[:2] == "__":
            continue
    print(name_def)
