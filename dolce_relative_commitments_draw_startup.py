import pickle
import pylab as plt
import networkx
from networkx.drawing.nx_pydot import graphviz_layout

from processors.graphisers.graph_creator import create_graph_from_relative_commitments
from processors.graphisers.graph_helpers import get_transitive_reduction_for_graph

dolce_relative_commitments_graph = create_graph_from_relative_commitments(relative_commitments_file_path='dolce_genuine_only_relative_commitments.pickle')
transitively_closed_dolce_relative_commitments_graph = networkx.transitive_closure(dolce_relative_commitments_graph)
transitively_reduced_dolce_relative_commitments_graph = get_transitive_reduction_for_graph(graph=dolce_relative_commitments_graph)
for edge, edge_attributes in networkx.get_edge_attributes(transitively_closed_dolce_relative_commitments_graph, name='definition').items():
    print(edge, edge_attributes)
# pos = networkx.planar_layout(transitively_reduced_dolce_relative_commitments_graph)
# networkx.draw(transitively_reduced_dolce_relative_commitments_graph, with_labels=True, pos=pos)
# plt.show()

# out_degrees = transitively_closed_dolce_relative_commitments_graph.out_degree()
# for node in transitively_closed_dolce_relative_commitments_graph:
#     descendants = networkx.descendants(transitively_closed_dolce_relative_commitments_graph, node)
#     sub_transitively_closed_dolce_relative_commitments_graph = transitively_closed_dolce_relative_commitments_graph.subgraph(descendants)
#     pos = networkx.fruchterman_reingold_layout(sub_transitively_closed_dolce_relative_commitments_graph)
#     networkx.draw(sub_transitively_closed_dolce_relative_commitments_graph, with_labels=True, pos=pos)
#     plt.savefig('images/'+str(node)+'.png', format="PNG")

# for (node, out_degree) in out_degrees:
#     print(node, len(transitively_closed_dolce_relative_commitments_graph.edges(node)))
# all_paths_in_transitively_closed_dolce_relative_commitments_graph = networkx.all_shortest_paths(transitively_closed_dolce_relative_commitments_graph)
# print(str(transitively_closed_dolce_relative_commitments_graph))
# print(networkx.to_dict_of_dicts(transitively_closed_dolce_relative_commitments_graph))
# for edge in transitively_closed_dolce_relative_commitments_graph.edges:
#     print(edge)
# # relative_commitments = pickle.load(open('relative_commitments.pickle', 'rb'))
#
# cycles_in_relative_commitment_graph = networkx.find_cycle(relative_commitment_graph)
# uncycled_relative_commitment_graph = relative_commitment_graph.copy()
# uncycled_relative_commitment_graph.remove_edges_from(networkx.simple_cycles(uncycled_relative_commitment_graph))
# v=0
# transitievly_reduced_relative_commitment_graph = networkx.transitive_reduction(uncycled_relative_commitment_graph)
# pos = networkx.spring_layout(transitively_closed_dolce_relative_commitments_graph, k=7)
# networkx.draw(transitively_closed_dolce_relative_commitments_graph, with_labels=True, pos=pos)
# plt.show()

# networkx.draw_networkx(dolce_relative_commitments_graph, arrows = True, node_shape = 's')
# plt.show()