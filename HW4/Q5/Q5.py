# https://www.geeksforgeeks.org/iterative-depth-first-traversal/
# Normal BFS + DFS non-recursive
from collections import defaultdict 

class Graph: 

    def __init__(self,Number): 
        self.graph = defaultdict(list) 
        self.numberOfNodes = Number
        self.bfs=[]
        self.dfs=[]
    def addEdge(self,u,v,w): 
        if v not in self.graph[u]:
            self.graph[u].append(v) 
            self.graph[v].append(u)
  
    def BFS(self, s): 
  

        visited = [False] * (self.numberOfNodes) 

        queue = [] 

        queue.append(s) 
        visited[s] = True
  
        while len(queue)!=0: 
  
            s = queue.pop(0) 
            self.bfs.append(s)
        
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
        print(self.bfs)
        
  
    def DFS(self,s): 
        visited = [False] *(self.numberOfNodes)
 
        stack = [] 
 
        stack.append(s)  
  
        while (len(stack)):  
 
            s =  stack.pop() 

            if (not visited[s]):  
                self.dfs.append(s)
#                 print(s,end=' ') 
                visited[s] = True 
    
            for node in self.graph[s]:  
                if (not visited[node]):  
                    stack.append(node)  
            
#         print(self.dfs)
        
        
if __name__ == "__main__":
    

    f = open("NYC.txt","r")
    x = f.readlines()
    number_of_nodes = int(x[0])
    number_of_edges = int(x[1])
    new_york = Graph(number_of_nodes)
    for i in range(number_of_edges):
        a = x[2+i].split()
        u = int(a[0])
        v = int(a[1])
        w = float(a[2])
        new_york.addEdge(u,v,w)

    new_york.graph

    new_york.DFS(1)
    new_york.BFS(1)
# output prints the entire BFS traversal array and the DFS traversal array
    print(new_york.dfs)
    print(new_york.bfs)




