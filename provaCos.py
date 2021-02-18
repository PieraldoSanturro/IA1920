class Graph:
    def __init__(self):
        self.nodes={}
        self.visited = False
        self.discovered = False


    def vertices(self):
        return self.nodes.keys()

    def __len__(self):
        return len(self.nodes)

    def adj(self,u):
        if u in self.nodes:
            return self.nodes[u]

    def insertNode(self,u):
        if u not in self.nodes:
            self.nodes[u]={}


    def insertEdge(self,u,v,w):
        self.insertNode(u)
        self.insertNode(v)
        self.nodes[u][v]=w





def bfs(g,radix):

    queue=[radix]

    while queue:
        u=queue.pop(0)
        u.visited=True
        for v in G.adj(u):
            if not v.visited:
                queue.append(v)
    return queue




if __name__=='__main__':

    g = Graph()
    for u, v, w in [('a', 'b', 3), ('a', 'd', 2), ('b', 'c', 5), ('c', 'd', 9), ('c', 'e', 1), ('d', 'e', 4)]:
       g.insertEdge(u, v, w)

    #for u in g.vertices():
     #   print(u, "->", g.adj(u))

    #print(g.vertices)

    bfs(g,'a')
