#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an item in the list

    Args:
        my_list: the list to delete from
        idx: the index to remove from

    Returns:
        new list or old list if error
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list)
    del my_list[idx]
    return (my_list)
