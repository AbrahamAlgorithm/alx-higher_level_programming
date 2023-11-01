#!/usr/bin/python3
def magic_calculation(a, b, c):
    """magic calculation solution part 2"""
    if a < b:
        return (c)
    else:
        if c > b:
            return (a + b)
    return (a * b - c)
