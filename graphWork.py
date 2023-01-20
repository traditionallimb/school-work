class Graph:
    def __init__(self, graphDict=None):
        if graphDict is None:
            graphDict = []
        self.graphDict = graphDict
    # get the keys of the dictionary
    def getVertices(self):
        return list(self.graphDict.keys())

    # add the vertex as a key
    def addVertex(self, vertex):
        if vertex not in self.graphDict:
            self.graphDict[vertex] = []

    def getEdges(self):
        return self.findEdges()

    # find a distinct list of edges
    def findEdges(self):
        edgeName = []
        for vertex in self.graphDict:
            for nextVertex in self.graphDict[vertex]:
                if {nextVertex, vertex} not in edgeName:
                    edgeName.append({vertex, nextVertex})
        return edgeName

    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graphDict:
            self.graphDict[vertex1].append(vertex2)
        else:
            self.graphDict[vertex1] = [vertex2]



graphElements = {
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}
g = Graph(graphElements)
print(g.getVertices())
print(g.getEdges())
g.addVertex("f")
print(g.getVertices())
g.addEdge({'f', 'a'})
g.addEdge({'f', 'e'})
print(g.getEdges())