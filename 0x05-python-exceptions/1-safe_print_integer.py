#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = isinstance(value, int)
        if x:
            print("{:d}".format(value))
            return True
    except TypeError:
        return False
