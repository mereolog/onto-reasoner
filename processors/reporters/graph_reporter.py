from networkx.classes import Graph


def report_edge_aggregations_as_tabular(graph: Graph, report_file_path: str, cast_to_latex=True):
    report_map = dict()
    for edge in graph.edges:
        source_node = edge[0]
        target_node = edge[1]
        if cast_to_latex:
            source_node = source_node.to_latex(True)
            target_node = target_node.to_latex(True)
        else:
            source_node = str(source_node)
            target_node = str(target_node)
        if source_node in report_map:
            outgoing_nodes = report_map[source_node]
        else:
            outgoing_nodes = list()
            report_map[source_node] = outgoing_nodes
        if not target_node in outgoing_nodes:
            outgoing_nodes.append(target_node)
    
    report_map = dict(sorted(report_map.items()))
    with open(file=report_file_path, mode='w') as report_file:
        for node, outgoing_nodes in report_map.items():
            outgoing_nodes.sort()
            outgoing_nodes_string = ', '.join(outgoing_nodes)
            print(node, r' & ', outgoing_nodes_string, r' \\', file=report_file)