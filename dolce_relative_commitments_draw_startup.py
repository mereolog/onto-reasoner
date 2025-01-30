import pickle
import pylab as plt
import networkx
from networkx.drawing.nx_pydot import graphviz_layout

from processors.graphisers.graph_creator import create_graph_from_relative_commitments
from processors.graphisers.graph_helpers import get_transitive_reduction_for_graph

dolce_relative_commitments_graph = create_graph_from_relative_commitments(relative_commitments_file_path='relative_commitments.pickle')
transitively_closed_dolce_relative_commitments_graph = networkx.transitive_closure(dolce_relative_commitments_graph)
# transitively_reduced_dolce_relative_commitments_graph = get_transitive_reduction_for_graph(graph=dolce_relative_commitments_graph)
for node in transitively_closed_dolce_relative_commitments_graph.nodes:
    node_paths = networkx.single_source_shortest_path(G=transitively_closed_dolce_relative_commitments_graph, source=node)
    print(node, node_paths)
# all_paths_in_transitively_closed_dolce_relative_commitments_graph = networkx.all_shortest_paths(transitively_closed_dolce_relative_commitments_graph)

# relative_commitments = pickle.load(open('relative_commitments.pickle', 'rb'))
#
# cycles_in_relative_commitment_graph = networkx.find_cycle(relative_commitment_graph)
# uncycled_relative_commitment_graph = relative_commitment_graph.copy()
# uncycled_relative_commitment_graph.remove_edges_from(networkx.simple_cycles(uncycled_relative_commitment_graph))
# v=0
# transitievly_reduced_relative_commitment_graph = networkx.transitive_reduction(uncycled_relative_commitment_graph)
# pos = networkx.arf_layout(transitively_closed_dolce_relative_commitments_graph)
# networkx.draw(transitively_closed_dolce_relative_commitments_graph, with_labels=True, pos=pos)
# plt.show()