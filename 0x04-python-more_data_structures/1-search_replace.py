#!/usr/bin/python3
def search_replace(my_list, search, replace):
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
