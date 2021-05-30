import networkx as nx
import matplotlib.pyplot as pl
from networkx.drawing.nx_agraph import to_agraph

class Graph:
    def __init__(self,adjMatrix,size):
        self.matrix = adjMatrix
        self.size = size
        self.graph = nx.MultiDiGraph()
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
        self.graph.add_nodes_from([i for i in (1,self.size) ])
        for i in range(0,self.size):
            for j in range(0, self.size):
                if self.matrix[i][j] == 1 and not (self.graph.has_edge(i+1,j+1) or self.graph.has_edge(j+1,i+1)):
                    self.graph.add_edge(i+1,j+1)
        self.graph.graph['edge'] = {'arrowsize': '0', 'splines': 'curved'}
        self.graph.graph['node'] = {'style':'filled','fillcolor':'blue'}
        graphicGraph = to_agraph(self.graph)
        graphicGraph.layout("dot")
        graphicGraph.draw("graphPath.png")

    def drawPath(self,pathArray=[]):
        arrayReturn = pathArray
        start = arrayReturn[0]
        if(len(arrayReturn)>1 and (self.matrix[start-1][pathArray[1]-1] == 1 or self.matrix[pathArray[1]-1][start-1]==1)):
            if(self.graph.has_edge(start,pathArray[1])):
                self.graph.remove_edge(start,pathArray[1])
                self.graph.add_edge(start,pathArray[1],color='red')
            if(self.graph.has_edge(pathArray[1],start)):
                self.graph.remove_edge(pathArray[1],start)
                self.graph.add_edge(pathArray[1],start,color='red')            
            graphicGraph = to_agraph(self.graph)
            graphicGraph.layout("dot")
            graphicGraph.draw("graphPath.png")
            return self.drawPath(arrayReturn[1:])
        elif (len(arrayReturn)<=1):
            return
        else:
            self.graph.graph['edge'] = {'arrowsize': '0', 'splines': 'curved','color': 'black'}
            return False
        

            
    
    def printAdjMatrix(self):
        for row in range(self.size):
            for column in range (self.size):
                if(column == self.size-1):
                    print(f"|{self.matrix[row][column]}|")
                else:
                    print(f"|{self.matrix[row][column]}|",end="")

