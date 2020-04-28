# directed Djikstras
import math
from collections import defaultdict 

class Graph:  
    def __init__(self,Number): 
  
        self.graph = defaultdict(list) 
        self.edgeTo = {}
        self.numberOfNodes = Number
        self.pathhelper=[]
        self.auxdistTo=[float('inf')]*self.numberOfNodes
        self.distTo=[float('inf')]*self.numberOfNodes
        
 
    def addEdge(self,u,v,w): 
        self.graph[u].append([v,w])
    
    def minimum(self,a,b):
        if a<=b:
            return a
        else:
            return b
        
    def Djikstra(self,source):
        self.pathhelper.append(source)
        self.distTo[source]=0
        self.edgeTo[source]=0
        
        while True:
            if self.distTo[source]==float('inf'):
                break
            for i in self.graph[source]:
                
                if (self.distTo[source]+i[1])<=self.auxdistTo[i[0]]:
                    self.auxdistTo[i[0]]=self.distTo[source]+i[1]
                    self.edgeTo[i[0]]=(source,i[0])
                else:
                    pass
            print("infinity") #added to show the loop runs infinitely
            a=self.auxdistTo.index(min(self.auxdistTo))
            source = a
            if self.auxdistTo[source]<self.distTo[source]:
                self.distTo[source]=self.auxdistTo[source]
            self.auxdistTo[source]=float('inf')
            if source not in self.pathhelper:
                self.pathhelper.append(source)
            
            if len(self.pathhelper)==self.numberOfNodes:
                break
            
        print(self.distTo)
           
        print(self.edgeTo)

if __name__ == "__main__":
    

    g = Graph(8) 
    g.addEdge(4,5,0.35) 
    g.addEdge(5,4,-0.66) 
    g.addEdge(4,7,0.37)
    g.addEdge(5,7,0.28)
    g.addEdge(7,5,0.28)
    g.addEdge(5,1,0.32)
    g.addEdge(0,4,0.38)
    g.addEdge(0,2,0.26)
    g.addEdge(7,3,0.39)
    g.addEdge(1,3,0.29)
    g.addEdge(2,7,0.34)
    g.addEdge(6,2,0.40)
    g.addEdge(3,6,0.52)
    g.addEdge(6,0,0.58)
    g.addEdge(6,4,0.93)

    g.Djikstra(0)
