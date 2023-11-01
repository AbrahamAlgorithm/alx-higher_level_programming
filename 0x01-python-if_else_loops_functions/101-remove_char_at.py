#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ''
    for i in range(len(str)):
        if i == n:
            continue
        else:
            newstr = newstr + str[i]
    return (newstr)
