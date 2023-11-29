#!/usr/bin/python3
"""
Print the name of a user
"""


def say_my_name(first_name, last_name=""):
    """a program to print name

    first_name: the firstname string
    last_name: the second string

    Raises:
        TypeError: if first_name is not instance of str
        TypeError: if last_name is not intance of str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
