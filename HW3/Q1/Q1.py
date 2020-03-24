#!/usr/bin/env python
# coding: utf-8
# References: Symbol Table slides
RED = True
BLACK = False

# Main definition of a Node in the BST
class Node:
    def __init__ (self,key,value,color):
        self.right = None
        self.left = None
        self.key = key
        self.value=value
        self.count = 1
        self.color = color
# Main Definition of Left Leaning Red-Black BST    
class BST:
    def __init__(self):
        self.root = None
    
    def isRed(self,N):
        if (N==None):
            return False
        return N.color == RED
    
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
            return x
        
    def rotateRight(self,N1):
        if self.isRed(N1.left):
            x= N1.left
            N1.left = x.right
            x.right= N1
            x.color = N1.color
            N1.color= RED
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
               
            if self.isRed(N.right) and not self.isRed(N.left):
                N=self.rotateLeft(N)
            if self.isRed(N.left) and self.isRed(N.left.left):
                N = self.rotateRight(N)
            if self.isRed(N.left) and self.isRed(N.right):
                self.flipColor(N)
            return N
        
        self.root = put1(self.root,key,value)
        self.root.color = BLACK
        
#  Calling sorted array feom BST by inorder traversal   
def inorder(n1): 
    if n1:
        inorder(n1.left)
        print(n1.key,n1.color)
        inorder(n1.right)



if __name__ == "__main__":
    pass
    b= BST()
    # using dataset given
    file1 = open("select-data.txt","r")
    list1 = file1.readlines()
    for i in range(len(list1)):
        list1[i] = int(list1[i])

    # arr1=['s','e','a','r','c','h','e','x','a','m','p','l','e']

    for i in range(len(list1)):
    #     print(i)
        b.put(list1[i],i)

    # for i in range(len(arr1)):
    #     print(i)
    #     b.put(arr1[i],i)
    inorder(b.root)





