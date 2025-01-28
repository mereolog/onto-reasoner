import sys

from processors.investigators.commitment_finders import find_relative_commitments
from processors.investigators.ontology_leaf_predicate_finder import find_subsumption_leaf_predicates

dolce_file_path='resources/midputs/dolce.cl'
reasoner_artifacts_path='resources/midputs/reasoner_artifacts/'

subsumption_leaf_predicates = (
    find_subsumption_leaf_predicates(
        theory_file_path=dolce_file_path,
        reasoner_artifacts_path=reasoner_artifacts_path))
print(subsumption_leaf_predicates)
sys.exit(-1)
find_relative_commitments(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path,
    subsumption_leaf_predicates=subsumption_leaf_predicates)