import networkx as nx
import matplotlib.pyplot as plt

# create a simple graph
G = nx.complete_bipartite_graph(5,3)

## --------- ##
## EXAMPLE 1 ##
## --------- ##

plt.title('Just draw, without touching the options')
nx.draw(G)
#plt.savefig('Plot_Examples1.png')
plt.show()

## --------- ##
## EXAMPLE 2 ##
## --------- ##

# we can create a dictionary and pass the options as a parameter;
options = {
    'node_color' : 'black',
    'node_size' : 100,
    'width' : 3,
}
plt.title(r'node color : black, node size : 100, width : 3')
nx.draw(G, **options)
#plt.savefig('Plot_Examples2.png')
plt.show()

## --------- ##
## EXAMPLE 3 ##
## --------- ##

options = {

}
