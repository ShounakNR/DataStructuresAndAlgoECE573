# used the code in slides to formulate my code

import time

file1 = open("8192pair.txt",'r')# have to manually change the filename to get the reading
list1 = file1.readlines()

pArr =[]
qArr = []
for i in list1:
    x = i.split()
    pArr.append(int(x[0]))
    qArr.append(int(x[1]))

MainArr=[]
for i in range(0,8192):
    MainArr.append(i)

# connetion/find
def findfunc (p,q):
    if MainArr[p] == MainArr[q]:
        return True

def union (p,q):
    pid = MainArr[p]
    qid = MainArr[q]
    for i in range(0, len(MainArr)):
        if MainArr[i]==pid:
            MainArr[i] = qid
start_time = time.time()
for i in range(0, len(pArr)):
    if findfunc(pArr[i],qArr[i]):
        continue
    else:
        union(pArr[i],qArr[i])  
        print ("union done for {} and {}".format(pArr[i],qArr[i]))   
print("time taken is {}".format(time.time()-start_time))
