import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

plt.subplot(121)
nx.draw(G, with_labels = True, font_weight = 'bold')

plt.subplot(122)
nx.draw_shell(G, nlist = [range(5, 10), range(5)], with_labels = True, font_weight = 'bold')

plt.savefig('Petersen_Graph_1.png')
plt.show()

# adding new layout options:

# create a dictionary that will be passed as a parameter
options = {
    'node_color' : 'black',
    'node_size' : 100,
    'width' : 3,
}

plt.subplot(221)
nx.draw_random(G, **options)
plt.title('Random plot')

plt.subplot(222)
nx.draw_shell(G, **options)
plt.title('Shell plot')

plt.subplot(223)
nx.draw_circular(G, **options)
plt.title('Circular plot')

plt.subplot(224)
nx.draw_spectral(G, **options)
plt.title('Spectral plot')

plt.savefig('Petersen_Graph_2.png')
plt.show()