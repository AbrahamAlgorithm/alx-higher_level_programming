#!/usr/bin/python3
def roman_to_int(roman_string):
    """Roman to Int

    Args:
        roman_string: the roman string

    Returns:
        the arabic numeral
    """
    if type(roman_string) != str or roman_string is None:
        return (0)
    roman = ['M', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX',
             'V', 'IV', 'I']
    arabic = [1000, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    length = len(roman_string)
    number = 0
    a = 0
    while length != 0:
        if length == 1:
            idx = roman.index(roman_string[a])
            number += arabic[idx]
            return (number)
        try:
            idx = roman.index(roman_string[a: a + 2])
            number += arabic[idx]
            length -= 2
            a += 2
        except ValueError:
            idx = roman.index(roman_string[a])
            number += arabic[idx]
            length -= 1
            a += 1
    return (number)
