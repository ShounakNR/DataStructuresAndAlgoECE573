#  used inspiration from lecture slides
file = open("dataset-problem2-hw2/data1.8192","r")

list1 = []

for i in file.readlines():
    list1.append(int(i))
import math
import time

#list1 = [1,2,4,6,3,5,45,10,8,77,23]
#list1 = [1,3,45,6,2,4,77,23,5,8,10]
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

def shellSort(arr): 
  
    start = time.time()
    n = len(arr) 
    gap = maxH(n)
  
    count=0 
    while gap > 0: 
  
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
    end = time.time()
    
    print(arr)
    print(count)
    print(end-start)

shellSort(list1)
#print(decH(1))
#print(count)