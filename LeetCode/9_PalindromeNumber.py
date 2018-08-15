#!/usr/bin/python

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
"""

def palindromeNumber(number):
    if(str(number)==str(number)[::-1]):
        return True
    else:
        return False

def palindromeNumber2(number):
    return True if str(number)==str(number)[::-1] else False

def main():
    number=12321
    print palindromeNumber(number)

if __name__=="__main__":
    main()