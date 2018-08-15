#!/usr/bin/python

"""
Boilerplate code.
"""


def main():
    try:
        numberOfElements=int(raw_input())
    except ValueError:
        print "Enter an integer"

if __name__=="__main__":
    main()