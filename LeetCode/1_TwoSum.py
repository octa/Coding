#!/usr/bin/python

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(list, target):
    hashMap={}
    for i in range(len(list)):
        if target-list[i] in hashMap:
            return[hashMap[target-list[i]], i]
        hashMap[list[i]]=i

def main():
    list=[2, 7, 11, 15]
    target=9
    print twoSum(list, target)

if __name__=="__main__":
    main()