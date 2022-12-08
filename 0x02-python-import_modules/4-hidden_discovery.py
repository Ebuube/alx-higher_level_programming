#!/usr/bin/python3
"""
A program that prints all the names defined by the compiled module
hidden_4.pyc (downloaded locally)
"""


if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name_def in names:
        if name_def[:2] != "__":
            continue
            print(name_def)
