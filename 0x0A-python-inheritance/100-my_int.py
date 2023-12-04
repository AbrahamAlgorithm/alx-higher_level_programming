#!/usr/bin/python3
"""MyInt inverted eq and does not equal"""


class MyInt(int):
    """hange == and !="""

    def __ne__(self, value):
        """revert equal"""
        return (self.real == value)

    def __eq__(self, value):
        """revert not equal"""
        return (self.real != value)
