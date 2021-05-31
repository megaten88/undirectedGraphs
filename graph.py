from os import remove
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.cycles import simple_cycles
from networkx.classes import graph
from networkx.drawing.nx_agraph import to_agraph

class Graph:
    def __init__(self, adjMatrix, size):
        self.matrix = adjMatrix
        self.size = size
        self.graph = nx.MultiDiGraph()
        
    def __len__(self):
        return self.size

    def getGraphDegrees(self):
        degreeArray = []
        totalDegree = []        
        visited = []                                                                                                                                                                                                                        
        for i in range(0, self.size):
            degreeArray.append(sum(self.matrix[i]))
        for i in range(0,self.size):
            add = 0
            for j in range(0,self.size):
                if(self.matrix[i][j]==1 and (f"{i}-{j}" not in visited and f"{j}-{i}" not in visited)):
                    visited.append(f"{i}-{j}")
                    add = add+1
            totalDegree.append(add)
        maxDegree = max(degreeArray)
        minDegree = min(degreeArray)
        sumDegree = sum(totalDegree)
        return (maxDegree, minDegree, sumDegree)

    def addEdge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 1
        self.matrix[vertex2][vertex1] = 1

    def removeEdge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 0
        self.matrix[vertex2][vertex1] = 0
 
    def generateGraph(self):
        self.graph.add_nodes_from([i for i in (1, self.size)])
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.matrix[i][j] == 1 and not (self.graph.has_edge(i+1, j+1) or self.graph.has_edge(j+1, i+1)):
                    self.graph.add_edge(i+1, j+1,color="black")
                elif((self.matrix[i][j]==1) and self.graph.has_edge(i+1, j+1)):
                    self.graph.remove_edge(i+1,j+1)
                    self.graph.add_edge(i+1, j+1,color="black")
                elif((self.matrix[i][j]==1) and self.graph.has_edge(j+1, i+1)):
                    self.graph.remove_edge(j+1,i+1)
                    self.graph.add_edge(j+1, i+1,color="black")
                elif((self.matrix[i][j]==0) and self.graph.has_edge(i+1, j+1)):
                    self.graph.remove_edge(i+1,j+1)
                    
        self.graph.graph['edge'] = {'arrowsize': '0', 'splines': 'curved', 'color': 'black'}
        self.graph.graph['node'] = {'style': 'filled', 'fillcolor': 'blue'}
        graphicGraph = to_agraph(self.graph)
        graphicGraph.layout("dot")
        graphicGraph.draw("graph.png")

    def drawPath(self, pathArray=[]):
        arrayReturn = pathArray
        start = arrayReturn[0]
        if(len(arrayReturn) > 1 and (self.matrix[start-1][pathArray[1]-1] == 1 or self.matrix[pathArray[1]-1][start-1] == 1)):
            if(self.graph.has_edge(start, pathArray[1])):
                self.graph.remove_edge(start, pathArray[1])
                self.graph.add_edge(start, pathArray[1], color='red')
            if(self.graph.has_edge(pathArray[1], start)):
                self.graph.remove_edge(pathArray[1], start)
                self.graph.add_edge(pathArray[1], start, color='red')
            graphicGraph = to_agraph(self.graph)
            graphicGraph.layout("dot")
            graphicGraph.draw("graphPath.png")
            return self.drawPath(arrayReturn[1:])
        elif (len(arrayReturn) <= 1):
            return True
        else:
            self.graph.graph['edge'] = {'arrowsize': '0', 'splines': 'curved', 'color': 'black'}
            return False

    def getAdjMatrix(self):
        return self.matrix

    def printAdjMatrix(self):
        for row in range(self.size):
            for column in range(self.size):
                if(column == self.size-1):
                    print(f"|{self.matrix[row][column]}|")
                else:
                    print(f"|{self.matrix[row][column]}|", end="")
    
    def isCyclic(self):
        return simple_cycles(self.graph)!= None
