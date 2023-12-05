#!/usr/bin/python3
"""return JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """to json strinf

    Args:
        my_obj: the python data structure

    Returns:
        thr json object representation
    """
    return (json.dumps(my_obj))
