#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary.update({key: value})
    else:
        a_dictionary.update({key: value})
    for i in a_dictionary:
        print("{:s}: {}".format(i, a_dictionary[i]))
