#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = value / 1
        print(int(x))
        return True
    except TypeError:
        return False
