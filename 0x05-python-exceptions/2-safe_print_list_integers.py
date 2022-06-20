#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        arr = [my_list[i] for i in range(x) if isinstance(my_list, int)]
        for i in arr:
            count += 1
            print("{:d}".format(i), end="")
        print(end="\n")
        return count
    except Exception as e:
        print(e)
