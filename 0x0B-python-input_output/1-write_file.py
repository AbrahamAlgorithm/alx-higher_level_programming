#!/usr/bin/python3
"""overwrite the content of the byte"""


def write_file(filename="", text=""):
    """write to file

    Args:
        filename: the filename
        text: the text

    Returns:
        return the number of byte written
    """
    with open(filename, 'w', encoding="utf-8") as myfile:
        return (myfile.write(text))
