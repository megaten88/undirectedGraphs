from graph import Graph
import tkinter as tk


size = int(input("set size: "))

adjMatrix = []
for i in range(size):
    adjMatrix.append([0 for i in range(size)])

mainGraph = Graph(adjMatrix,size)
mainGraph.addEdge(1,2)
mainGraph.addEdge(1,3)
mainGraph.addEdge(1,4)
mainGraph.addEdge(4,1)
mainGraph.addEdge(4,2)
mainGraph.addEdge(4,3)
mainGraph.addEdge(3,1)
mainGraph.addEdge(3,2)
mainGraph.addEdge(3,4)
mainGraph.addEdge(2,1)
mainGraph.addEdge(2,3)
mainGraph.addEdge(2,4)
mainGraph.addEdge(2,2)
mainGraph.printAdjMatrix()
print(mainGraph.getGraphDegrees())
mainGraph.generateGraph()
mainGraph.drawPath([4,2,1])

window.mainloop()
