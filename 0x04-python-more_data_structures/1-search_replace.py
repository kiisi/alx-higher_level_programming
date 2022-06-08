#!/usr/bin/python3
def search_replace(my_list, search, replace):
    arr = []
    for x in my_list:
        if x == search:
            x = replace
        arr.append(x)
    return arr
