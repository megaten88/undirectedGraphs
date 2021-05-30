import networkx as nx
import matplotlib.pyplot as pl
from networkx.drawing.nx_agraph import to_agraph

class Graph:
    def __init__(self,adjMatrix,size):
        self.matrix = adjMatrix
        self.size = size

    def __len__(self):
        return self.size

    def getGraphDegrees(self):
        degreeArray = []
        for i in range(0,self.size):
            degreeArray.append(sum(self.matrix[i]))
        maxDegree = max(degreeArray)
        minDegree = min(degreeArray)
        sumDegree = sum(degreeArray)
        return (maxDegree,minDegree, sumDegree)

    def addEdge(self,vertex1,vertex2):
        self.matrix[vertex1-1][vertex2-1] = 1

    def generateGraph(self):
        graph = nx.MultiDiGraph()
        graph.add_nodes_from([i for i in (1,self.size) ])
        for i in range(0,self.size):
            for j in range(0, self.size):
                if self.matrix[i][j] == 1 and not (graph.has_edge(i+1,j+1) or graph.has_edge(j+1,i+1)):
                    graph.add_edge(i+1,j+1)
        graph.graph['edge'] = {'arrowsize': '0', 'splines': 'curved'}
        graph.graph['node'] = {'style':'filled','fillcolor':'blue'}
        graphicGraph = to_agraph(graph)
        graphicGraph.layout("dot")
        graphicGraph.draw("graph.png")
    
    def printAdjMatrix(self):
        for row in range(self.size):
            for column in range (self.size):
                if(column == self.size-1):
                    print(f"|{self.matrix[row][column]}|")
                else:
                    print(f"|{self.matrix[row][column]}|",end="")

