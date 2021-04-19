#!/usr/bin/python

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
"""

def reverse(number):

    reverse=0
    sign=True if number>0 else False
    number=number if sign else -number
    while(number>0):
        remainder=number%10
        number=number/10
        reverse=reverse*10+remainder

    reverse=reverse if sign else -reverse
    if -2 ** 31 <= reverse <= 2 ** 31 - 1:
        return reverse
    else:
        return 0


def main():
    number=1563847412
    print reverse(number)

if __name__=="__main__":
    main()