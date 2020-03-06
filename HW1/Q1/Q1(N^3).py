# https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
# https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
# assuing that the 3 sum should be equal to 0
import time

file1 = open("8int.txt",'r')# have to manually change the filename to get the reading
list1 = file1.readlines()
list1 = [int(i) for i in list1]
count=0
c=0
# start_time = time.time()
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        for k in range(j+1,len(list1)):
            count+=1
            if list1[i]+list1[j]+list1[k]==0:
               c+=1
# print(time.time()-start_time)
print(count)
# print(list1)