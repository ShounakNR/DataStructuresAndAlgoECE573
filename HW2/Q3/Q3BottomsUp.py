#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:36:04 2020
https://www.geeksforgeeks.org/iterative-merge-sort/
@author: shounakrangwala
"""


file = open("dataset-problem2-hw2/data1.1024","r")
list1 = []

for i in file.readlines():
    list1.append(int(i))

import math
import time
count =0
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
    mergeSizeMax=len(arr)/2
    N=len(arr)
    print(N)

    size=1
    while (size<=mergeSizeMax+1):

        for i in range(0,N,size*2):   
            high = min(i+size*2-1,N-1)
            if high == i+size*2-1:
                mid = i+(high-i)//2
            else:
                mid = i+size-1
            merge(arr,aux,i,mid,high)
            
        size=size*2

aux = makeaux(list1)
        
start = time.time()   
sort(list1,0,len(list1)-1)
end = time.time()
print(list1)
print(count)
print(end-start)               