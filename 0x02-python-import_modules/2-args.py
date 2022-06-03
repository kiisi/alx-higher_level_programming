#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arglist = sys.argv
    if len(arglist) <= 1:
        print("0 argument")
    else:
        if(len(arglist) - 1 == 1):
            myArg = 'argument'
        else:
            myArg = 'arguments'
        print("{} {}".format(len(arglist) - 1, myArg))
        for i in range(1, len(arglist)):
            print("{}: {}".format(i, arglist[i]))
