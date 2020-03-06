#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:54:22 2020
https://www.geeksforgeeks.org/python-program-for-quicksort/
@author: shounakrangwala
"""
import random
import time

file = open("dataset-problem2-hw2/data1.1024","r")
list1 = []

for i in file.readlines():
    list1.append(int(i))

#list1 = [1,3,45,6,2,4,77,23,5,8,10]
#
def shuffle(arr):
    random.shuffle(arr)



def swap(arr,a,b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp


def medianOf3(arr,low,mid,high):
    if arr[low] < arr[high]:
        if arr[mid] <= arr[high]:
            return mid
        else:
            return high
    elif arr[low] > arr[high]:
        if arr[low] >= arr[mid]:
            return mid
        else:
            return low
    elif arr[low] > arr[mid]:
        if arr[high] <= arr[low]:
            return high
        else:
            return low
    elif arr[low] < arr[mid]:
        if arr[high] >= arr[mid]:
            return mid
        else:
            return high
    elif arr[low] == arr[high] == arr[mid]:
        return mid         

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[j] >= pivot and i < j:
            j-=1
        if j!=i:
            arr[i] = arr[j] 
            i+=1
        while arr[i] < pivot and i < j:
            i += 1
        if j!=i:
            arr[j] = arr[i]   
            j-=1
    
    arr[i] = pivot
    return i

def sort (arr,low,high):        
    if high<low:
        return 
    
    median = medianOf3(arr,low,low+(high-low)//2,high)
#    print(median)
    swap(arr,low,median)
#    print(low,high)
    x= partition(arr,low,high)
    sort(arr,low,x-1)
    sort(arr,x+1,high)
    
#shuffle(list1)
#print(list1)
low  = 0
high = len(list1)-1
start = time.time()
sort(list1,low,high)
end = time.time()
print(list1)
print(end-start)
