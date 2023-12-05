#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """append to the file

    Args:
        filename: the filename
        text: what to append

    Returns:
        the number of bytes
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        return (myfile.write(text))
