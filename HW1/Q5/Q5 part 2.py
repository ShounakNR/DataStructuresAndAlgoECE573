import time
start_time = time.time()
list1 = [10,-10,-5,5,3,-3,4,6,0,-7,7]
# list1 = [-10,0,10]
def sort(ListInput):
    for i in range (0,len(ListInput)):
        minIndex = i
        for j in range(i+1,len(ListInput)):
            if ListInput[j]<ListInput[i]:
                minIndex = j
                ListInput[i],ListInput[minIndex] = ListInput[minIndex],ListInput[i]   
    return ListInput    

def numPairs (list1, element,lowest=0,highest=len(list1)-1):
    # lowest = 0
    # highest = len(list1)-1
    count = 0
    while highest>lowest:
        Twosum = list1[lowest]+list1[highest]
        if Twosum+element>0:
            highest = highest-1
        elif  Twosum+element<0:
            lowest = lowest+1
        else:
            lowest = lowest+1
            highest = highest-1
            count+=1
    return count

list1= sort(list1)
print(list1)
Count=0
for i in range(0,len(list1)):
    # print(numPairs(list1,list1[i],i+1,len(list1)-1))
    Count += numPairs(list1,list1[i],i+1,len(list1)-1)
print (Count)
print(time.time()-start_time)