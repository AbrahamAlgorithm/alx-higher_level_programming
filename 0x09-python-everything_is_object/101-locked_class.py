#!/usr/bin/python3
"""Locking a class against props"""


class LockedClass:
    """creating a locked class that
    prevens creaion of another prop
    """

    __slots__ = ["first_name"]
