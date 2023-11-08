#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search a list and replace it with replace

    Args:
        my_list: the list to search through
        search: the element to search for
        replace: the elemnt to replace it

    Returns:
        the new list with replace element
    """
    new_list = []
    if my_list is None:
        return (None)
    if len(my_list) == 0:
        return ([])
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(i)
    return (new_list)
