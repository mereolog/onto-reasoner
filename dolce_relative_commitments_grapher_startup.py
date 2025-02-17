import networkx
from matplotlib import pyplot as plt
from networkx.classes import DiGraph

from processors.graphisers.graph_creator import create_graph_from_relative_commitments
from processors.graphisers.graph_helpers import get_transitive_reduction_for_graph
from processors.investigators.predicates_finder import find_all_predicates, find_n_ary_predicates
from processors.reporters.graph_reporter import report_edge_aggregations_as_tabular

dolce_unary_predicates = find_n_ary_predicates('resources/midputs/dolce.cl', arity=1)

dolce_relative_commitments_multigraph = create_graph_from_relative_commitments(relative_commitments_file_path='resources/outputs/pickles/dolce_relative_commitments.pickle')

for dolce_predicate in dolce_unary_predicates:
    if not dolce_predicate in dolce_relative_commitments_multigraph.nodes:
        dolce_relative_commitments_multigraph.add_node(dolce_predicate)
        print(dolce_predicate, 'is isolated.')

dolce_relative_commitments_digraph = DiGraph(dolce_relative_commitments_multigraph)
transitively_closed_dolce_relative_commitments_graph = networkx.transitive_closure(dolce_relative_commitments_digraph)
transitively_reduced_dolce_relative_commitments_graph = get_transitive_reduction_for_graph(dolce_relative_commitments_digraph)

def stringizer(object) -> str:
    return str(object)

dolce_graph_pos = networkx.spectral_layout(dolce_relative_commitments_digraph)
networkx.draw(dolce_relative_commitments_digraph, with_labels=True, pos=dolce_graph_pos)
networkx.write_graphml(dolce_relative_commitments_digraph, 'resources/outputs/reports/images/Dolce relative commitments.graphml')
networkx.write_gml(dolce_relative_commitments_digraph, 'resources/outputs/reports/images/Dolce relative commitments.gml', stringizer=stringizer)

plt.savefig('resources/outputs/reports/images/Dolce relative commitments.png')
plt.close()
report_edge_aggregations_as_tabular(
    graph=dolce_relative_commitments_digraph,
    report_file_path='resources/outputs/reports/images/Dolce transitively closed relative commitments.txt',
    cast_to_latex=False)

dolce_closed_graph_pos = networkx.circular_layout(transitively_closed_dolce_relative_commitments_graph)
networkx.draw(transitively_closed_dolce_relative_commitments_graph, with_labels=True, pos=dolce_closed_graph_pos)
plt.savefig('resources/outputs/reports/images/Dolce transitively closed relative commitments.png')
plt.close()

dolce_reduced_graph_pos = networkx.shell_layout(transitively_reduced_dolce_relative_commitments_graph)
networkx.draw(transitively_reduced_dolce_relative_commitments_graph, with_labels=True, pos=dolce_reduced_graph_pos)
plt.savefig('resources/outputs/Dolce transitively reduced relative commitments.png')
plt.close()

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
