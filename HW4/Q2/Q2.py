
from collections import defaultdict 
import time
class KGraph:  
    def __init__(self,Number): 
  
        self.graph = defaultdict(list) 
        self.numberOfNodes = Number
        self.group = [0]*(self.numberOfNodes)
        self.Connected=[]
        self.treeedges=0
        self.Tree=[]
        for i in range(self.numberOfNodes):
            self.Connected.append(i)
 
    def addEdge(self,u,v,w): 
        self.graph[(u,v)]=w
#         self.graph[v].append(u) #UNDIRECTED
    
        

    def sortGraph(self):
        dict1=defaultdict(list)
        for i in sorted(self.graph.items(), key=lambda item: item[1]):
            dict1[i[0]]=i[1]
        self.graph = dict1
#         print(self.graph)
       
    def unionfind(self,u,v):
        if self.Connected[u]!=self.Connected[v]:
            x=self.Connected[u]
            for j in range(self.numberOfNodes):
                if self.Connected[j]==x:
                    self.Connected[j]=self.Connected[v]
            return True
        else:
            return False
            
    
    def KruskalMST(self):
        self.sortGraph()
        
        count=0
        starttime = time.time()
        while self.treeedges<self.numberOfNodes-1:
            for i in self.graph:
                u=i[0]
                v=i[1]
#                 print(u,v)
                if self.unionfind(u,v):
#                     print(self.Connected)
                    self.treeedges+=1
                    self.Tree.append([i,self.graph[i]])
        endtime = time.time()
        print("The time for Kruskal to run is {} secs.".format(endtime-starttime))
        print("The Kruskal MST is as follows: {} ".format(self.Tree))


class PGraph:  
    def __init__(self,Number): 
  
        self.graph = defaultdict(list) 
        self.auxgraph = defaultdict(list) 
        self.numberOfNodes = Number
        self.connected=[0]
        self.Tree=[]
        self.pqarr=[float('inf')]*self.numberOfNodes
        
 
    def addEdge(self,u,v,w): 
        self.graph[u].append([v,w])
        self.graph[v].append([u,w]) #UNDIRECTED
        self.auxgraph[(v,w)].append(u)
        self.auxgraph[(u,w)].append(v)
    
    def minimum(self,a,b):
        if a<=b:
            return a
        else:
            return b
        
    def PrimsMST(self):
        for i in self.graph[0]:
            self.pqarr[i[0]] = i[1]
        starttime = time.time()
        while len(self.connected)<self.numberOfNodes:
    
            a= self.pqarr.index(min(self.pqarr))
            zz = self.auxgraph[(a,min(self.pqarr))]

            self.Tree.append([zz[0],a])
            self.connected.append(a)
            self.pqarr[a]=float('inf')
            for j in self.graph[a]:
                if j[0] not in self.connected:
                    self.pqarr[j[0]] = self.minimum(self.pqarr[j[0]],j[1])
        endtime = time.time()
        print("The time for Prims to run is {} secs.".format(endtime-starttime))
        print("The Prims' MST is as follows: {} ".format(self.Tree))


if __name__ == "__main__":
        
    f = open("Q1Q2.txt","r")
    x = f.readlines()
    number_of_nodes = int(x[0])
    number_of_edges = int(x[1])
    kru = KGraph(number_of_nodes)
    pri = PGraph(number_of_nodes)
    for i in range(number_of_edges):
        a = x[2+i].split()
        u = int(a[0])
        v = int(a[1])
        w = float(a[2])
        kru.addEdge(u,v,w)
        pri.addEdge(u,v,w)
# output is the runtime and the MST edges for both Prims and Krushkals
    kru.KruskalMST()

    pri.PrimsMST()




