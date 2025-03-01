import networkx
from networkx.classes import DiGraph

from processors.graphisers.graph_creator import create_graph_from_relative_commitments
from processors.graphisers.graph_helpers import get_transitive_reduction_for_graph, report_cycles_in_graph
from processors.investigators.predicates_finder import find_n_ary_predicates, \
    calculate_theory_signature_count
from processors.reporters.graph_reporter import report_edge_aggregations_as_tabular
from startup_commons import dolce_file_path

def stringizer(object) -> str:
    return str(object)


dolce_unary_predicates = find_n_ary_predicates('resources/midputs/dolce.cl', arity=1)

dolce_relative_commitments_multigraph = (
    create_graph_from_relative_commitments(
        relative_commitments_file_path='resources/outputs/pickles/dolce_genuine_only_relative_commitments.pickle'))

for dolce_predicate in dolce_unary_predicates:
    if not dolce_predicate in dolce_relative_commitments_multigraph.nodes:
        dolce_relative_commitments_multigraph.add_node(dolce_predicate)
        print(dolce_predicate, 'is isolated.')

dolce_relative_commitments_digraph = DiGraph(dolce_relative_commitments_multigraph)
report_cycles_in_graph(dolce_relative_commitments_digraph)
transitively_closed_dolce_relative_commitments_graph = networkx.transitive_closure(dolce_relative_commitments_digraph)
transitively_reduced_dolce_relative_commitments_graph = get_transitive_reduction_for_graph(dolce_relative_commitments_digraph)

networkx.write_gml(dolce_relative_commitments_digraph, 'resources/outputs/reports/images/dolce relative commitments.gml', stringizer=stringizer)
networkx.write_gml(transitively_closed_dolce_relative_commitments_graph, 'resources/outputs/reports/images/closed dolce relative commitments.gml', stringizer=stringizer)
networkx.write_gml(transitively_reduced_dolce_relative_commitments_graph, 'resources/outputs/reports/images/reduced dolce relative commitments.gml', stringizer=stringizer)

report_edge_aggregations_as_tabular(
    graph=transitively_closed_dolce_relative_commitments_graph,
    report_file_path='resources/outputs/reports/dolce transitively closed relative commitments.txt',
    cast_to_latex=True)

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
