import networkx
from networkx.classes import DiGraph


def remove_cycles_from_graph(graph: DiGraph) -> DiGraph:
    cycleless_graph = graph.copy()
    cycles = networkx.simple_cycles(graph)
    cycleless_graph.remove_edges_from(cycles)
    return cycleless_graph


def get_transitive_reduction_for_graph(graph: DiGraph) -> DiGraph:
    cycleless_graph = remove_cycles_from_graph(graph=graph)
    transitively_reduced_graph = networkx.transitive_reduction(cycleless_graph)
    return transitively_reduced_graph