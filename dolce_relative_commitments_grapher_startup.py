import networkx
from matplotlib import pyplot as plt
from networkx.classes import DiGraph

from processors.graphisers.graph_creator import create_graph_from_relative_commitments
from processors.graphisers.graph_helpers import get_transitive_reduction_for_graph
from processors.reporters.graph_reporter import report_edge_aggregations_as_tabular

dolce_relative_commitments_multigraph = create_graph_from_relative_commitments(relative_commitments_file_path='resources/outputs/pickles/dolce_relative_commitments.pickle')
dolce_relative_commitments_digraph = DiGraph(dolce_relative_commitments_multigraph)
transitively_closed_dolce_relative_commitments_graph = networkx.transitive_closure(dolce_relative_commitments_digraph)
transitively_reduced_dolce_relative_commitments_graph = get_transitive_reduction_for_graph(dolce_relative_commitments_digraph)

dolce_graph_pos = networkx.arf_layout(dolce_relative_commitments_digraph, a=1.5)
networkx.draw(dolce_relative_commitments_digraph, with_labels=True, pos=dolce_graph_pos)
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
