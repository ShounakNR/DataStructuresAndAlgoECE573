# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
# https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
# assuing that the 3 sum should be equal to 0
import time

file1 = open("8192int.txt","r")
list1 = file1.readlines()
list1 = [int(i) for i in list1]
count=0
# print(list1)

def sort(ListInput):
    for i in range (0,len(ListInput)):
        minIndex = i
        for j in range(i+1,len(ListInput)):
            if ListInput[j]<ListInput[i]:
                minIndex = j
                ListInput[i],ListInput[minIndex] = ListInput[minIndex],ListInput[i]   
    return ListInput    

def binSearch(ListInput, low, high, ele):
    if low<=high:
        mid = int((high-low)/2)

        if ListInput[mid]==ele:
            return True

        elif ListInput[mid]>ele:
            return binSearch(ListInput,low,mid-1,ele)
        
        else :
            return binSearch(ListInput,mid+1,high,ele)

    else:
        return False
list1 = sort(list1)

# print(binSearch(list1,0,len(list1)-1,692))
count = 0
start_time = time.time()
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if binSearch(list1,0,len(list1)-1,-(list1[i]+list1[j])):
            count+=1
        
print(time.time()-start_time)
print (count)


