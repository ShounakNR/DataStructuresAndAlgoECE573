# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# Undirected graph cycle detection
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict,deque

class Graph:  
    def __init__(self,Number): 
        self.graph = defaultdict(list) 
        self.numberOfNodes = Number
        self.preorder=[]
        self.hasCycle= False
 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u)


        
    def DFSUtil(self,before, v, visited,count): 
            visited[v]= True
            self.preorder.append(v)
            for i in self.graph[v]: 
#                 checking for cycles
                if visited[i]==True and i!=before:
                    self.hasCycle=True

                if visited[i] == False: 
                    self.DFSUtil(v,i, visited,count) 
    
    def DFS(self):  
        V = len(self.graph)
        self.preorder=[]
        visited =[False]*(self.numberOfNodes) 
        count = 0 
        before = None
        for i in range(V): 
            cycleVisited=[0]
            if visited[i] == False: 
                count +=1
                self.DFSUtil(before,i, visited,count) 



if __name__ == "__main__":
    
    f = open("Q1Q2.txt","r")
    x = f.readlines()
    number_of_nodes = int(x[0])
    number_of_edges = int(x[1])
    
    new_york = Graph(number_of_nodes)
    for i in range(number_of_edges):
        a = x[2+i].split()
        u = int(a[0])
        v = int(a[1])
        new_york.addEdge(u,v)

    new_york.DFS()
# outputs a boolean if the graph has a cycle or not
    print(new_york.hasCycle)


