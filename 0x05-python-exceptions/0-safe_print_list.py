#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            return my_list[i]
    except IndexError:
        return 
