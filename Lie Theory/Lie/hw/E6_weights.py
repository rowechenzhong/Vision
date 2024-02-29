"""
Today, we will be manually enumerating the 27-dimensional
representation of E6.

"""

# We will be drawing some diagrams
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# The Cartan matrix of E6 is:

cartan = np.array([
    [2, -1, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0],
    [0, -1, 2, -1, 0, -1],
    [0, 0, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, 0],
    [0, 0, -1, 0, 0, 2]
])

# Dynkin weights are represented as vectors of 6 elements.

weights = [
    np.array([1, 0, 0, 0, 0, 0])
]


heights = [0]
height_idx = [0]
height_counts = [1] + [0] * 100

hashes = []


def hash(a):
    # add all ternary representation of the vector
    # to the set of hashes
    res = 0
    for i in range(6):
        res += a[i] * 3 ** i
    return res


hashes.append(hash(weights[0]))

# We will now compute the weights of the 27-dimensional representation
# by DFS-ing.

edges = []
edge_labels = []

i = 0
while i < len(weights):
    for j in range(6):
        # if the j-th entry is positive, we can subtract the j-th simple root
        if weights[i][j] > 0:
            new_weight = weights[i] - cartan[j]
            h = hash(new_weight)
            if h not in hashes:
                weights.append(new_weight)
                hashes.append(h)
                edges.append((i, len(weights) - 1))
                edge_labels.append(j)
                d = heights[i] + 1
                heights.append(d)
                height_idx.append(height_counts[d])
                height_counts[d] += 1
            else:
                # get index of new_weight
                k = hashes.index(h)
                edges.append((i, k))
                edge_labels.append(j)
    i += 1

# print all the weights
for w in weights:
    print(w)


assert len(weights) == 27

plt.figure(figsize=(10, 3))
# title: blue, green
params = {
    'E6': [[0, 1, 2, 3, 4, 5], []],
    'E6_SO10': [[0, 1, 2, 3, 5], [4]],
    'E6_SU5': [[0, 1, 2, 3], [5]],
    'E6_SU2SU3': [[0, 1, 3], [2]],
}

for name, (blue, green) in params.items():
    G = nx.DiGraph()
    G.add_edges_from(edges)
    pos = {}
    for i, w in enumerate(weights):
        pos[i] = (heights[i], (height_idx[i] + 0.5) /
                  (height_counts[heights[i]]))
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color='r')

    green_edges = [i for i, j in enumerate(edge_labels) if j in green]
    blue_edges = [i for i, j in enumerate(edge_labels) if j in blue]
    nx.draw_networkx_edges(G, pos, edgelist=[edges[i] for i in blue_edges],
                           arrows=True, edge_color='b')
    nx.draw_networkx_edges(G, pos, edgelist=[edges[i] for i in green_edges],
                           arrows=True, edge_color='g')
    plt.savefig("{}.png".format(name))
    plt.clf()
