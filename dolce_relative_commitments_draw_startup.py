import pickle
import pylab as plt
import networkx
from networkx.drawing.nx_pydot import graphviz_layout

relative_commitment_graph = pickle.load(open('relative_commitment_graph.pickle', 'rb'))
cycles_in_relative_commitment_graph = networkx.find_cycle(relative_commitment_graph)
uncycled_relative_commitment_graph = relative_commitment_graph.copy()
uncycled_relative_commitment_graph.remove_edges_from(networkx.simple_cycles(uncycled_relative_commitment_graph))
v=0
transitievly_reduced_relative_commitment_graph = networkx.transitive_reduction(uncycled_relative_commitment_graph)
pos = networkx.graphviz_layout(transitievly_reduced_relative_commitment_graph, equidistant=True, resolution=2)
networkx.draw(transitievly_reduced_relative_commitment_graph, with_labels=True, pos=pos)
plt.show()