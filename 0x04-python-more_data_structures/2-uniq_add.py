#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add uniue member of a list

    Args:
        my_list: the list to add from

    Returns:
        the addition result
    """
    if len(my_list) == 0 or my_list is None:
        return (0)
    uniq = sorted(set(my_list))
    return (sum(uniq))
