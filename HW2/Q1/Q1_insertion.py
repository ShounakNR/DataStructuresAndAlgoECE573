#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:57:12 2020
used inspiration from lecture slides
@author: shounakrangwala
"""

file = open("dataset-problem2-hw2/data1.8192","r")

list1 = []

for i in file.readlines():
    list1.append(int(i))
import math
import time

#list1 = [1,2,4,6,3,5,45,10,8,77,23]
#list1 = [1,3,45,6,2,4,77,23,5,8,10,21,23,4,2,456,654,4,789,234,235,567,34,89,86,34]
N= len(list1)
#count = 0
#print(N)
def maxH (size): 
    i =1
    h=0
    while(i<math.log2(N+1)):
        h = pow(2,i)-1
#        print(h)
        i+=1
    return h

def decH (i):
    return pow(2,math.log2(i+1)-1)-1


def insertionSort(arr):
#    count=0
    for i in range(0,len(arr)):
#        count+=1
        h = arr[i]
        j=i-1
        while j>=0 and h < arr[j]:
#            count+=1
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=h
#    return count

def shellSort(arr): 
  
    start = time.time()
    n = len(arr) 
    gap = maxH(n)
  
    count=0 
    while gap>=8: 
  
        for i in range(gap,n): 
            temp = arr[i] 
            j = i 
            count+=1
            while  j >= gap and arr[j-gap] >temp: 
                count+=1
                arr[j] = arr[j-gap] 
                j -= gap 
            arr[j] = temp 
        gap = int(decH(gap))
    
    print(insertionSort(arr))
    end = time.time()
    print(end-start)
    print(arr)


shellSort(list1)
#print(decH(1))
#print(count)