#!/usr/bin/python3
"""object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """from json string to python data structure

    Args:
        my_str: the json string

    Returns:
        the python data structure
    """
    return (json.loads(my_str))
