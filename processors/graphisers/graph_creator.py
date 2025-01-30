import pickle

from networkx.classes import DiGraph


def create_graph_from_relative_commitments(relative_commitments_file_path: str) -> DiGraph:
    graph = DiGraph()
    relative_commitments = pickle.load(open(relative_commitments_file_path, 'rb'))
    for relative_commitment in relative_commitments:
        graph.add_edge(
            relative_commitment.committing_predicate,
            relative_commitment.committed_predicate,
            definition=relative_commitment.definition)
    return graph