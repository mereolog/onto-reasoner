import networkx
from networkx.classes import DiGraph

from processors.graphisers.graph_creator import create_graph_from_relative_commitments
from processors.graphisers.graph_helpers import get_transitive_reduction_for_graph

dolce_relative_commitments_graph = create_graph_from_relative_commitments(relative_commitments_file_path='dolce_relative_commitments.pickle')
transitively_closed_dolce_relative_commitments_graph = networkx.transitive_closure(DiGraph(dolce_relative_commitments_graph))
transitively_reduced_dolce_relative_commitments_graph = get_transitive_reduction_for_graph(graph=DiGraph(dolce_relative_commitments_graph))
# print(len(transitively_closed_dolce_relative_commitments_graph.edges))
# print(len(networkx.get_edge_attributes(transitively_closed_dolce_relative_commitments_graph, name='definition')))
commitments_map = dict()
for edge in transitively_closed_dolce_relative_commitments_graph.edges:
    if edge[0].to_latex(True) in commitments_map:
        committed_categories = commitments_map[edge[0].to_latex(True)]
    else:
        committed_categories = list()
        commitments_map[edge[0].to_latex(True)] = committed_categories
    if not edge[1].to_latex(True) in committed_categories:
        committed_categories.append(edge[1].to_latex(True))
commitments_map = dict(sorted(commitments_map.items()))
for committing_category, commited_categories in commitments_map.items():
    commited_categories.sort()
    commited_categories_string = ', '.join(commited_categories)
    print(committing_category, r' & ', commited_categories_string, r' \\')
    
# # relative_commitment_reports = dict()
# # for edge, edge_attributes in networkx.get_edge_attributes(dolce_relative_commitments_graph, name='ground').items():
# #     if [edge[0], edge[1]] in relative_commitment_reports:
# #         relative_commitment_reports[[edge[0], edge[1]]].append(edge_attributes)
# #     else:
# #         relative_commitment_reports[[edge[0], edge[1]]] = [edge_attributes]
# out_degrees = dolce_relative_commitments_graph.out_degree()
# print(list(out_degrees))
# # v=0
# # pos = networkx.planar_layout(transitively_reduced_dolce_relative_commitments_graph)
# # networkx.draw(transitively_reduced_dolce_relative_commitments_graph, with_labels=True, pos=pos)
# # plt.show()
#
out_degrees = transitively_closed_dolce_relative_commitments_graph.out_degree()
out_degree_map = dict()
for category, out_degree in out_degrees:
    if out_degree in out_degree_map:
        categories = out_degree_map[out_degree]
    else:
        categories = list()
        out_degree_map[out_degree] = categories
    categories.append(category.to_latex(True))
out_degree_map = dict(sorted(out_degree_map.items()))

for out_degree, categories in out_degree_map.items():
    categories.sort()
    categories_string = ', '.join(categories)
    print(str(out_degree), r' & ', categories_string, r' \\')
    

# # for node in transitively_closed_dolce_relative_commitments_graph:
# #     descendants = networkx.descendants(transitively_closed_dolce_relative_commitments_graph, node)
# #     sub_transitively_closed_dolce_relative_commitments_graph = transitively_closed_dolce_relative_commitments_graph.subgraph(descendants)
# #     pos = networkx.fruchterman_reingold_layout(sub_transitively_closed_dolce_relative_commitments_graph)
# #     networkx.draw(sub_transitively_closed_dolce_relative_commitments_graph, with_labels=True, pos=pos)
# #     plt.savefig('images/'+str(node)+'.png', format="PNG")
#
# # for (node, out_degree) in out_degrees:
# #     print(node, len(transitively_closed_dolce_relative_commitments_graph.edges(node)))
# # all_paths_in_transitively_closed_dolce_relative_commitments_graph = networkx.all_shortest_paths(transitively_closed_dolce_relative_commitments_graph)
# # print(str(transitively_closed_dolce_relative_commitments_graph))
# # print(networkx.to_dict_of_dicts(transitively_closed_dolce_relative_commitments_graph))
# # for edge in transitively_closed_dolce_relative_commitments_graph.edges:
# #     print(edge)
# # # relative_commitments = pickle.load(open('relative_commitments.pickle', 'rb'))
# #
# # cycles_in_relative_commitment_graph = networkx.find_cycle(relative_commitment_graph)
# # uncycled_relative_commitment_graph = relative_commitment_graph.copy()
# # uncycled_relative_commitment_graph.remove_edges_from(networkx.simple_cycles(uncycled_relative_commitment_graph))
# # v=0
# # transitievly_reduced_relative_commitment_graph = networkx.transitive_reduction(uncycled_relative_commitment_graph)
# pos = networkx.spring_layout(dolce_relative_commitments_graph, k=7)
# networkx.draw(dolce_relative_commitments_graph, with_labels=True, pos=pos)
# plt.show()

# networkx.draw_networkx(dolce_relative_commitments_graph, arrows = True, node_shape = 's')
# plt.show()