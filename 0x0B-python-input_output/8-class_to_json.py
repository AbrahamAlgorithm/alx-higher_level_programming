#!/usr/bin/python3
"""convert class to json"""


def class_to_json(obj):
    """class to json

    Args:
        obj: instance of the class
    """
    return (obj.__dict__)
