#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:02:11 2020

@author: shounakrangwala
"""

#list1 = [4,3,2,1]
file = open("dataset-problem2-hw2/data1.4096","r")

list1 = []
count =0
for i in file.readlines():
    list1.append(int(i))
import math
import time



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
                count+=mid-i+1
                
            else:
                aux[k]=arr[i]
                i+=1
        elif i > mid:
            aux[k]=arr[j]
            j+=1
        elif j > high:
            aux[k]=arr[i]
            i+=1
    
    for m in range(low,high+1):
        arr[m]=aux[m]

def sort(arr,low,high):
    
    if high<=low:
        return 0

    mid = low+(high-low)//2

    sort(arr,low,mid)
    sort(arr,mid+1,high)
    merge(arr,aux,low,mid,high)
  
start = time.time()
aux = makeaux(list1)  
sort(list1,0,len(list1)-1)
end = time.time()
print(list1)
print(count)
print(end-start)               