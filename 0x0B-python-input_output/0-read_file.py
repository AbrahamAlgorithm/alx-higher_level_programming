#!/usr/bin/python3
"""read element from the file"""


def read_file(filename=""):
    """read element to the file

    Args:
        filename: the file name
    """
    with open(filename, encoding="utf-8") as myfile:
        line = myfile.readlines()
        for i in line:
            print(i, end='')
