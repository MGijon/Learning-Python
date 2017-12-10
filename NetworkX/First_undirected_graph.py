import networkx as nx

# Create an undirected empty graph
G = nx.Graph()

## NODES:
## =====

# Adding a node directly
G.add_node(1)

# We can also add nodes from a list of nodes
G.add_nodes_from([x for x in range(2, 6)])


## EDGES:
## =====

# Directly
G.add_edge(1, 2)

e = (2, 3) # define a tuple
G.add_edge(*e) # unpack the tuple


# We add them grom a list of tuples
G.add_edges_from([(3, 4), (1, 5)])
