import numpy as np
import matplotlib.pyplot as plt
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

    

# Create a graph from the adjacency matrix
graph = nx.from_numpy_array(matrix)

# Create a Figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Draw the graph on the first subplot
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, ax=ax1, with_labels=True)
ax1.set_title('Graph')

# Display the adjacency matrix as a binary grid on the second subplot
ax2.axis('off')  # Remove axis ticks and labels

# Create a binary grid based on the adjacency matrix
binary_grid = np.zeros_like(matrix)
binary_grid[matrix == 1] = 1

# Plot the binary grid
ax2.imshow(binary_grid, cmap='binary')
ax2.set_title('Adjacency Matrix')

# Display the plot
plt.tight_layout()
plt.show()