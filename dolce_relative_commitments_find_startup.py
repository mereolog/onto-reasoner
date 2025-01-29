import sys

import networkx
import matplotlib.pyplot as plt
import pickle

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.commitment_finders import find_relative_commitments
from processors.investigators.ontology_leaf_predicate_finder import find_subsumption_leaf_predicates

dolce_file_path='resources/midputs/dolce.cl'
reasoner_artifacts_path='resources/midputs/reasoner_artifacts/'

# subsumption_leaf_predicates = (
#     find_subsumption_leaf_predicates(
#         theory_file_path=dolce_file_path,
#         reasoner_artifacts_path=reasoner_artifacts_path))

find_relative_commitments(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path)

pickle.dump(RelativeCommitments.registry, open('relative_commitments.pickle', 'wb'))


# pickle.dump(relative_commitment_graph, open('relative_commitment_graph.pickle', 'wb'))
# relative_commitment_graph
# transitievly_reduced_relative_commitment_graph = networkx.transitive_reduction(relative_commitment_graph)
# pickle.dump(transitievly_reduced_relative_commitment_graph, open('transitievly_reduced_relative_commitment_graph.pickle', 'wb'))
# transitievly_closed_relative_commitment_graph = networkx.transitive_closure(relative_commitment_graph)
# pickle.dump(transitievly_closed_relative_commitment_graph, open('transitievly_closed_relative_commitment_graph.pickle', 'wb'))