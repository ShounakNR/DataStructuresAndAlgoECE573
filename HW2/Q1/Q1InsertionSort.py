#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:06:20 2020
used https://www.geeksforgeeks.org/python-program-for-insertion-sort/
@author: shounakrangwala
"""

file = open("dataset-problem2-hw2/data1.8192","r")

list1 = []

for i in file.readlines():
   list1.append(int(i))


import math
import time


N= len(list1)
#count = 0
#print(N)

def insertionSort(arr):
    count=0
    for i in range(0,len(arr)):
        count+=1
        h = arr[i]
        j=i-1
        while j>=0 and h < arr[j]:
            count+=1
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=h
        print(arr)
    return count



print(insertionSort(list1))
print(list1)
#print(decH(1))
#print(count)