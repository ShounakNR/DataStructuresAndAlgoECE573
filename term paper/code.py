# main string = B, target string  = A
#  implementing a code for searching the DNA sequencing thus the domain set will
# be only comprising of A,C,G,T.
A = "TACG"
B = "AATACCGATACGAACGTACGTT"
lengthTarget = len(A)
lenText = len(B)
m = 1073741789
b = 4
Hcommon = b**(lengthTarget-1) % m
result=[]
# convert each element into a integer
def referenceTable (x):
    dictionary = {'A':0,'C':1,"G":2,"T":3}
    return dictionary[x]
# assert the string comparison process
def equal (a):
    for i in range(0,lengthTarget):
        if B[a+i] != A[i]:
            return False
    return True
# calculate the hash for a string
def hashCalc(s):
    h=0
    for i in range(0,len(s)):
        h = (h * b + referenceTable(s[i])) % m
    return h

targetHash = hashCalc(A)
# Rabin-Karp Algo
def RKA():
    substringHash = hashCalc(B[:lengthTarget])
    if substringHash == targetHash:
        if equal(0):
            result.append(0)
    for i in range (0,lenText-lengthTarget):
        substringHash = (b* (substringHash-referenceTable(B[i])* Hcommon)+ referenceTable(B[i+lengthTarget]))% m
        if substringHash==targetHash:
            if equal(i+1):
                result.append(i+1)

RKA()
for i in range(len(result)):
# result has the index where the target string can be found
    print(result[i])