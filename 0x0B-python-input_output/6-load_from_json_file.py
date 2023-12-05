#!/usr/bin/python3
"""load python from json file string"""
import json


def load_from_json_file(filename):
    """load py data structure from file string

    Args:
        filename: the file name

    Returns:
        the python data structure
    """
    with open(filename, 'r') as myfile:
        return (json.load(myfile))
