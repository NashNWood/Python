# Python:   3.6.1
#
# Author:   Nash N. Wood
#
#Purpose:   The Tech Academy - Exercise 48
#           Write your own version of the sorted() method in Python.
#           This method should take a list as an argument and return
#           a list that is sorted in ascending order.
#
#===================================================================#



def bubbleSort(alist):
    for num in range(len(alist)-1,0,-1):
        for i in range(num):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [67,45,2,13,1,998]
bubbleSort(alist)
print(alist)


def bubbleSort(blist):
    for num in range(len(blist)-1,0,-1):
        for i in range(num):
            if blist[i]>blist[i+1]:
                temp = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp

blist = [89,23,33,45,10,12,45,45,45]
bubbleSort(blist)
print(blist)

