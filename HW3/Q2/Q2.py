#!/usr/bin/env python
# coding: utf-8
# References: https://www.coursera.org/lecture/analysis-of-algorithms/path-length-Bzppb + symbol slides demo
import random

RED = True
BLACK = False

# Main definition of Node of BST
class Node:
    def __init__ (self,key,value,color):
        self.right = None
        self.left = None
        self.key = key
        self.value=value
        self.count = 1
        self.color = color

# Same BST as Q1 but with extra method for average path calculation (assumed it to be the path from the root to each leaf node)
class BST:
    def __init__(self):
        self.root = None
    
    def isRed(self,N):
        if (N==None):
            return False
        return N.color == RED
    
    def size (self,N1):
        if N1 == None:
            return 0
        return N1.count
    
        
    def flipColor(self,N1):
        if not self.isRed(N1):
            if self.isRed(N1.left) :
                if self.isRed(N1.right):
                    N1.color = RED
                    N1.left.color = BLACK
                    N1.right.color = BLACK
                
    def rotateLeft(self,N1):
        if self.isRed(N1.right):
            x = N1.right
            N1.right=x.left
            x.left = N1
            x.color=N1.color
            N1.color=RED
            x.count = N1.count
            N1.count = 1 + self.size(N1.left) + self.size(N1.right)
            return x
        
    def rotateRight(self,N1):
        if self.isRed(N1.left):
            x= N1.left
            N1.left = x.right
            x.right= N1
            x.color = N1.color
            N1.color= RED
            x.count = N1.count
            N1.count = 1 + self.size(N1.left) + self.size(N1.right)
            return x
        
    def put(self,key,value):
        
        def put1(N,key,value):
            if N==None:
                N1 = Node(key,value,RED)
                return N1
            if key<N.key:
                N.left=put1(N.left,key,value)
            elif key>N.key:
                N.right=put1(N.right,key,value)
            else:
                N.value = value
    #             N.count = 1 + self.size(N.left) + self.size(N.right)  
            if self.isRed(N.right) and not self.isRed(N.left):
                N=self.rotateLeft(N)
            if self.isRed(N.left) and self.isRed(N.left.left):
                N = self.rotateRight(N)
            if self.isRed(N.left) and self.isRed(N.right):
                self.flipColor(N)
                
            N.count = 1 + self.size(N.left) +self.size(N.right)
            return N
        
        self.root = put1(self.root,key,value)
        self.root.color = BLACK
        
    
    def avgPathLen(self):
        def avgPathLen1(N1):
            List=[]
            avg = 0
            s =0
            if N1 != None:
                self.searchBST(N1,1,List)
            if len(List)>0:
                for i in range(len(List)):
                    s += List[i]
    #                 print(self.size(self.root),self.counterRed())
            avg = s/(self.size(self.root)- self.counterRed())
            return avg
        return avgPathLen1(self.root)
    
    def searchBST(self,x,length,list1):
        if self.isRed(x):
            if x.left != None:
                self.searchBST(x.left, length, list1)
            if x.right != None:
                self.searchBST(x.right, length, list1)
        else :
            list1.append(length)
            if x.left != None:
                self.searchBST(x.left, length + 1, list1)
            if x.right != None:
                self.searchBST(x.right, length + 1, list1)
    def counterRed(self):
        def count1(N,redl):
            if N == None:
                return
            if N.color == RED:
                redl.append(1)
            count1(N.left,redl)
            count1(N.right,redl)
        List2 = []
        count1(self.root,List2)
        return len(List2)

# Print the sorted dataset using inorder traversal
def inorder(n1): 
    if n1:
        inorder(n1.left)
        print(n1.key,n1.color,n1.count)
        inorder(n1.right)

# Make a BST with ordered input
def orderedInsert(size):
    b=BST()
    for i in range(size):
        b.put(i,i)
    return b

# Make a BST with random input
def randomInsert(size):
    b=BST()
    list1=[]
    for i in range(size):
        list1.append(i)
    random.shuffle(list1)
    for i in range(size):
        b.put(list1[i],i)
    return b

if __name__ == "__main__":
    
    sizeArr =[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192]
    # sizeArr =[256]
    for i in range(len(sizeArr)):
        avg_ordered = 0
        avg_random = 0
        b_ordered = orderedInsert(sizeArr[i])
        b_random = randomInsert(sizeArr[i])
    #     inorder(b_ordered.root)
    #     inorder(b_random.root)
    #     print (b_ordered.size(b_ordered.root))
        print(b_ordered.avgPathLen(),b_random.avgPathLen())





