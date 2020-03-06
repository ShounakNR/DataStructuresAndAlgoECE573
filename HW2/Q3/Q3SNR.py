#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:16:09 2020
https://www.geeksforgeeks.org/python-program-for-merge-sort/
@author: shounakrangwala
"""


file = open("dataset-problem2-hw2/data1.1024","r")
list1=[]

for i in file.readlines():
    list1.append(int(i))
import math
import time

count = 0

def makeaux(arr):
    aux=[]
    for i in range(len(arr)):
        aux.append(0)
    return aux

def merge (arr,aux,low, mid, high):

    i= low
    j=mid+1
    global count
    for k in range(low,high+1):
        if i<=mid and j<=high:
            if arr[i] > arr[j]:
                aux[k]=arr[j]
                j+=1
                count+=2
            else:
                aux[k]=arr[i]
                i+=1
                count+=2
        elif i > mid:
            aux[k]=arr[j]
            j+=1
            count+=2
        elif j > high:
            aux[k]=arr[i]
            i+=1
            count+=2
    
    for m in range(low,high+1):
        arr[m]=aux[m]
        count+=1

def sort(arr,low,high):
    if high<=low:
        return
    mid = low+(high-low)//2
#    print(mid)
    sort(arr,low,mid)
    sort(arr,mid+1,high)
    merge(arr,aux,low,mid,high)
    
aux = makeaux(list1)
start = time.time()   
sort(list1,0,len(list1)-1)
end = time.time()
print(list1)
print(count)
print(end-start)               