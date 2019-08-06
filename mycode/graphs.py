class graph:

    def __init__(self,gdict=None):
        if(gdict is None):
            gdict={}
        self.gdict=gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findEdges()

    def getEdges(self):
        edgename=[]
        for v in self.gdict:
            for ed in self.gdict[v]:
                if {v,ed} not in edgename:
                    edgename.append({v,ed})
        return edgename

    def addVertice(self,ver):
        if ver not in self.gdict:
            self.gdict[ver]=[]

    def addEdge(self,edge):
        (ver1,ver2)=tuple(edge)
        if ver1 in self.gdict:
            self.gdict[ver1].append(ver2)
        else:
            self.gdict[ver1]=[ver2]

    def dfs(self,start,visited=None):
        if(visited==None):
            visited=set()
        visited.add(start)
        print(start)
        for next in self.gdict[start] - visited:
            self.dfs(next,visited)

if __name__=='__main__':
    graph_elements = {"a": ["b", "c"],
                      "b": ["a", "d"],
                      "c": ["a", "d"],
                      "d": ["e"],
                      "e": ["d"]
                      }
    g=graph(graph_elements)
    print(g.getVertices())
    print(g.getEdges())

    g.addVertice("f")
    print(g.getVertices())
    print(g.getEdges())

    g.addEdge({'a','e'})
    print(g.getEdges())
    g.dfs('ax')



