import networkx as nx

# Create an undirected empty graph
G = nx.Graph()

## NODES:
## =====

# Adding a node directly
G.add_node(1)

# We can also add nodes from a list of nodes
G.add_nodes_from([x for x in range(2, 6)])

# You can also add nodes along with node attributes if your container yields 2-tuples (node, node_attribute_dict).
# Node attributes will be discussed later.

H = nx.path_graph(10)
G.add_nodes_from(H)

## EDGES:
## =====

# Directly
G.add_edge(1, 2)

e = (2, 3) # define a tuple
G.add_edge(*e) # unpack the tuple


# We add them grom a list of tuples
G.add_edges_from([(3, 4), (1, 5)])

# We can also add a 'ebunch' of edges. An ebunch is any iterable container of edge-tuples.
# An edge-tuple con be a 2-tuple of nodes or a 3-tuple woth 2 nodes followed by an edge attribute dictionary.
# Edge attributes will be discussed later.
#G.add_edges_from(H.edges)

## OBTAINING INFORMATION:
## ======================

print(G.number_of_nodes())         # Number of nodes
print(G.number_of_edges())         # Number of edges
print(list(G.nodes()))             # List of nodes
print(list(G.edges()))             # List of edges

print(G.adj[1])                    # or list(G.neighbors(1))
print(G.degree()[1])               # The number of edges incident to node 1


########################################################################################################################

G.clear()                         # removing all edges and nodes

G.add_edges_from([(1, 2), (3, 5)])
G.add_nodes_from([x for x in range(1, 11)])

# Nodes don't have to be numbers
G.add_node('Thing')               # add 'Thing' node
G.add_nodes_from('Thing')         # add modes 'T', 'h', 'i', 'n', 'g'
G.add_edge(3, 'T')


print(G.number_of_nodes())        # Number of nodes
print(G.number_of_edges())        # Number of edges

print(list(G.nodes()))            # List of nodes
print(list(G.edges()))            # List of edges

## VERY BASIC PLOTTING:
## ===================


import matplotlib.pyplot as plt
nx.draw(G)
plt.savefig('First_undirected_graph_example_1.png')
plt.show()