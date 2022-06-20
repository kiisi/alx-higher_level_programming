#!/usr/bin/python3

def safe_print_integer(value):
    try:
        x = int(value / 1)
        print("{:d}".format(x))
        return True
    except TypeError:
        return False
