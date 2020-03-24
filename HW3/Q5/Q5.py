#!/usr/bin/env python
# coding: utf-8

# References: symbol table slides
class Node:
    def __init__ (self,key,value):
        self.right = None
        self.left = None
        self.key = key
        self.value=value
        self.count = 1
        self.rank = None


class BST:
    def __init__(self):
        self.root = None
    def get(self,key):
        n1 = self.root

        while True:
            if key < n1.key:
                if n1.left==None:
                    return [n1,-1]
                else :
                    n1= n1.left
               
            elif key > n1.key:
                if n1.right==None:
                    return [n1,1]
                else :
                    n1 = n1.right
               
            else:
               
                return [n1,n1.key]
        
    
        
    def size (self,N1):
        if N1 == None:
            return 0
        return N1.count
       
    
#     def put(self,key,value):
#         if self.root.key == None:
#             self.root = Node(key,value)
#             return
#         if self.get(key)[1] == -1:
#             n2 = Node(key,value)
#             self.get(key)[0].left=n2
#         elif self.get(key)[1] == 1:
#             n2 = Node(key,value)
#             self.get(key)[0].right=n2
#         else:
#             self.get(key)[0].value = value
    def put(self,key,value):
        
        def put1(N,key,value):
            if N==None:
                N = Node(key,value)
                return N
            if key<N.key:
                N.left=put1(N.left,key,value)
            elif key>N.key:
                N.right=put1(N.right,key,value)
            else:
                N.value = value
            N.count = 1 + self.size(N.left) +self.size(N.right)
            return N
        self.root = put1(self.root,key,value)
        
    def rank (self,key):
        def rank1 (key1,N1):
            if N1 == None:
                return 0
            if key1 <N1.key:
                return rank1(key1,N1.left)
            elif key1 > N1.key:
                return rank1(key1, N1.right)+1+self.size(N1.left)
            else:
                return self.size(N1.left)
        return rank1(key,self.root)
    
    def select (self,rank):
        def select1(N1,rank1):
            if rank1<self.size(N1.left):
                return select1(N1.left,rank1)
            elif self.size(N1.left)==rank1:
                return N1.key
            else:
                return select1(N1.right,rank1-1-self.size(N1.left))
        return select1(self.root,rank)


def inorder(n1): 
    if n1:
        inorder(n1.left)
        print(n1.key)
        inorder(n1.right)


if __name__ == "__main__":
    
    file1 = open("select-data.txt","r")
    list1 = file1.readlines()
    for i in range(len(list1)):
        list1[i] = int(list1[i])

    b=BST()
    for i in range(len(list1)):
    #     print(i)
        b.put(list1[i],i)

    print("select(7) is: "+str(b.select(7)))
    print("rank(7) is:"+str(b.rank(7)))




