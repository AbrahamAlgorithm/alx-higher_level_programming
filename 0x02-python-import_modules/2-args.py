#!/usr/bin/python3

if __name__ == "__main__":
    """print the no. and value of CLD"""
    import sys

    argv = sys.argv
    b = len(argv) - 1
    if b == 0:
        print("0 arguments.")
    elif b == 1:
        print("{} argument:".format(b))
        print("{}: {}".format(b, argv[b]))
    elif b > 1:
        print("{} arguments:".format(b))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
