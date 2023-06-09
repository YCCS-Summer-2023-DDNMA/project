import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

import networkx as nx


def generate_random_graph(n,p=0.5):
    graph = np.zeros((n,n), dtype=int)
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


choice = int(input('Enter 0 to enter your own matrix or 1 to randomly generate one: '))

if choice == 1:
    size = int(input('Enter the desired graph size: '))
    matrix = generate_random_graph(size)
elif choice == 0:
    input_str = input('Enter your adjacency matrix: ')
    adj_matrix_str = input_str.replace(' ', '')
    adj_matrix_str = adj_matrix_str.strip('[]')
    rows = adj_matrix_str.split('],[')
    matrix = np.array([list(map(int, row.split(','))) for row in rows])
    size = matrix.shape[0]
else:
    print(choice,'is not a vaid choice.')
    exit()

def draw_adjacency_matrix(G, node_order=None, partitions=None, colors=None, ax=None):
    """
    Draw the adjacency matrix of a networkx graph.
    - G is a networkx graph.
    - node_order (optional) is a list of nodes, where each node in G
      appears exactly once.
    - partitions is a list of node lists, where each node in G appears
      in exactly one node list.
    - colors is a list of strings indicating what color each
      partition should be.
    - ax (optional) is the Axes object to draw the matrix on.
    If partitions is specified, the same number of colors needs to be
    specified.
    """
    adjacency_matrix = nx.to_numpy_array(G, dtype=bool, nodelist=node_order)

    # Plot adjacency matrix in toned-down black and white
    if ax is None:
        ax = plt.gca()
    ax.imshow(adjacency_matrix, cmap="Greys", interpolation="none")

    # The rest is just if you have sorted nodes by a partition and want to
    # highlight the module boundaries
    assert len(partitions) == len(colors)
    for partition, color in zip(partitions, colors):
        current_idx = 0
        for module in partition:
            ax.add_patch(patches.Rectangle((current_idx, current_idx),
                                           len(module),  # Width
                                           len(module),  # Height
                                           facecolor="none",
                                           edgecolor=color,
                                           linewidth="1"))
            current_idx += len(module)

# Create a graph from the adjacency matrix
graph = nx.from_numpy_array(matrix)

# Create a Figure and a single subplot grid with two columns
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Draw the graph on the first subplot
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, ax=axes[0], with_labels=True)
axes[0].set_title('Graph')

# Call the custom function to draw the adjacency matrix on the second subplot
draw_adjacency_matrix(graph, node_order=graph.nodes(), partitions=[], colors=[], ax=axes[1])


# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.3)

# Display the plot
plt.show()