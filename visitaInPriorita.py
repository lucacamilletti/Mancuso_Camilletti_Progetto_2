from priorityQueue.PQbinomialHeap import PQbinomialHeap
from graph.graph.Graph_AdjacencyList import GraphAdjacencyList

def PriorityVisit(graph):
    vMax = graph.getMaxWeightNode()
    vertexSet = PQbinomialHeap()  # nodes to explore
    vertexSet.insert(vMax.getId(), vMax.getWeight())
    markedNodes = {vMax.getId()}  # nodes already explored
    list = []


    while not vertexSet.isEmpty():
        IdNode = vertexSet.findMax()
        list.append(IdNode)
        vertexSet.deleteMax()
        adjNodes = graph.getAdj(IdNode)
        for nodeIndex in adjNodes:
            if nodeIndex not in markedNodes:
                Node = graph.getNode(nodeIndex)
                vertexSet.insert(Node.getId(), Node.getWeight())
                markedNodes.add(nodeIndex)
    return list

def graphGenerator():
    graph = GraphAdjacencyList()

    nodes = []
    node = graph.addNode(2, 81)
    nodes.append(node)
    node = graph.addNode(4, 22)
    nodes.append(node)
    node = graph.addNode(6, 12)
    nodes.append(node)
    node = graph.addNode(8, 32)
    nodes.append(node)
    node = graph.addNode(10, 26)
    nodes.append(node)
    node = graph.addNode(12, 14)
    nodes.append(node)
    node = graph.addNode(14, 40)
    nodes.append(node)
    node = graph.addNode(16, 7)
    nodes.append(node)
    node = graph.addNode(18, 6)
    nodes.append(node)
    node = graph.addNode(20, 4)
    nodes.append(node)



    graph.insertEdge(nodes[7].getId(), nodes[4].getId())
    graph.insertEdge(nodes[7].getId(), nodes[2].getId())
    graph.insertEdge(nodes[2].getId(), nodes[4].getId())
    graph.insertEdge(nodes[2].getId(), nodes[3].getId())
    graph.insertEdge(nodes[2].getId(), nodes[5].getId())
    graph.insertEdge(nodes[3].getId(), nodes[5].getId())
    graph.insertEdge(nodes[6].getId(), nodes[5].getId())
    graph.insertEdge(nodes[6].getId(), nodes[8].getId())
    graph.insertEdge(nodes[0].getId(), nodes[8].getId())
    graph.insertEdge(nodes[0].getId(), nodes[2].getId())
    graph.insertEdge(nodes[0].getId(), nodes[1].getId())
    graph.insertEdge(nodes[0].getId(), nodes[9].getId())
    graph.insertEdge(nodes[1].getId(), nodes[9].getId())

    graph.print()

    return graph

if __name__ == "__main__":
    grafo = graphGenerator()
    visita = PriorityVisit(grafo)
    print(visita)