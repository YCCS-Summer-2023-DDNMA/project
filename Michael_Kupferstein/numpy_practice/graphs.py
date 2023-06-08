import numpy as np
import matplotlib as plt

def generate_random_graph(n,p=0.5):
    graph = np.zeros((n,n), dtype=int)
    print(p)
    edges = generateRandomEdges(n,p) #generates a list of edges
    for e in edges:
        row = e[0]
        col = e[1]
        graph[row - 1][col - 1] = 1
        graph[col - 1][row - 1] = 1
    return graph


def generateRandomEdges(n,p):
    edges = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if np.random.random() < p:
                edges.append((i,j))
    return edges

