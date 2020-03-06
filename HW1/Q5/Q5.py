def numPairs (list1):
    lowest = 0
    highest = len(list1)-1
    count = 0
    while highest>lowest:
        if list1[lowest]+list1[highest]>0:
            highest = highest-1
        elif  list1[lowest]+list1[highest]<0:
            lowest = lowest+1
        else:
            
            lowest = lowest+1
            highest = highest-1
            count+=1
    return count
print(numPairs([-10,-5,-3,0,3,4,5,6,10]))