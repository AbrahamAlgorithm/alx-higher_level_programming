#!/usr/bin/python3
"""Locking a class against props"""


class LockedClass:
    """creating a locked class that
    prevents creat`ion of another prop
    """

    __slots__ = ["first_name"]
