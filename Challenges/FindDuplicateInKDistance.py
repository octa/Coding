#!/usr/bin/python

#Find if two elements are same K distance apart
#
#Example:
#
#list=[2, 5, 6, 7, 3, 2, 4, 1, 3] and k=4 should return True because the second 3 is the 4th elements after the first 3
#

def distance(list, k):

    hashMap=[]
    for i in range(len(list)):

        if k==1 and list[i] in hashMap and hashMap[0]==list[i]:
            return "Yes"


        if list[i] in hashMap and hashMap[0]==list[i]:
            return "Yes"

        if(i>=k):
            del hashMap[0]

        hashMap.append(list[i])

    return "No"

def main():
    list = [2, 5, 6, 7, 3, 2, 4, 1, 3]
    k=3
    print distance(list, k)

if __name__=="__main__":
    main()