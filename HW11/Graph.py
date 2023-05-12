from PQ import PriorityQueue
class Graph:
   def __init__(self, V=(), E=()):
       """Initializes Vertices and Edges"""
       self.V = set()
       self.E = set()
       self.neighbors = {}
      
       for v in V: self.add_vertex(v)
       for e in E:
           self.add_edge(e[0], e[1], e[2])
 
   def add_vertex(self, v):
       """Adds a vertex to the set of vertices"""
       self.V.add(v)
       self.neighbors[v] = {}
 
   def remove_vertex(self,v):
       """Removes a vertex from the set of vertices"""
       self.V.remove(v)
       del self.neighbors[v]
  
   def vertices(self):
       """Iterates through the vertices"""
       return iter(self.V)
 
   def wt(self, u, v):
       """Returns the weight"""
       return self.neighbors[u][v]
 
   def add_edge(self, u, v, wt):
       """Adds an edge with weight to the set of edges"""
       self.neighbors[u][v] = wt
       self.neighbors[v][u] = wt
 
   def remove_edge(self, u, v, wt):
       """Removes an edge from the set of edges"""
       del self.neighbors[u][v]
       del self.neighbors[v][u]
 
   def nbrs(self, v):
       """Returns all neighbors of the given vertex"""
       return iter(self.neighbors[v])
 
   def fewest_flights(self, city):
       """Returns the fewest amounts of flights using the Breadth First Search Algorithm"""
       t = {city: None}
       f = {city: 0}
       visit = [city]
 
       while visit:
           a = visit.pop(0)
           for nbr in self.neighbors[a]:
               if nbr not in t:
                   t[nbr] = a
                   f[nbr] = f[a] + 1
                   visit.append(nbr)
 
       return t, f
 
   def shortest_path(self, city):
       """Finds the minimum way to get to another city using Dijkstra's algorithm"""
       t = {city: None}
       D = {u: float('inf') for u in self.vertices()}
       D[city] = 0
       visit = PriorityQueue(entries = [(v,D[v]) for v in self.vertices()])
       for u in visit:
           for n in self.nbrs(u):
               if D[u] + self.wt(u,n) < D[n]:
                   D[n] = D[u] + self.wt(u,n)
                   t[n] = u
                   visit.changepriority(n,D[n])
       return t, D
  
   def minimum_salt(self, city): 
       """Returns the minimum spanning tree and distance using Prim's algorithm"""
       tree = {}
       D = {city: 0}
       visit = PriorityQueue()
       visit.insert((None, city), 0)
       for a, b in visit:
           if b not in tree:
               tree[b] = a
               if a is not None:
                   D[b] = self.wt(a, b)
               for nbr in self.nbrs(b):
                   visit.insert((b, nbr), self.wt(b, nbr))
 
       return tree, D

