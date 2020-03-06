# used the code in slides to formulate my code

import time

file1 = open("32pair.txt",'r')# have to manually change the filename to get the reading
list1 = file1.readlines()

pArr =[]
qArr = []
for i in list1:
    x = i.split()
    pArr.append(int(x[0]))
    qArr.append(int(x[1]))

MainArr=[]
sizeArr = []
for i in range(0,8192):
    MainArr.append(i)
    sizeArr.append(1)

def findRoot (i):
    while i != MainArr[i]:
        i = MainArr[i]
    return i   

def findfunc (p,q):
    if findRoot(p) == findRoot(q):
        return True
 

def union (p,q):
    pid = findRoot(p)
    qid = findRoot(q)
    MainArr[pid] = qid
    if sizeArr[pid]<=sizeArr[qid]:
        MainArr[pid] = qid
        sizeArr[qid] += sizeArr[pid]
    else:
        MainArr[qid] = pid
        sizeArr[pid] += sizeArr[qid]
    print ("union done for {} and {}".format(p,q))


start_time = time.time()
for i in range(0, len(pArr)):
    if findfunc(pArr[i],qArr[i]):
        continue
    else:
        union(pArr[i],qArr[i])
        
print("time taken is {}".format(time.time()-start_time))
        

