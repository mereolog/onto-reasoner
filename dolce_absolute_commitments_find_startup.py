import sys

from processors.investigators.commitment_finders import find_relative_commitments, find_absolute_commitments
from processors.investigators.subsumptions_finder import find_subsumption_leaf_predicates

dolce_file_path='resources/midputs/dolce.cl'
reasoner_artifacts_path='resources/midputs/reasoner_artifacts/'

find_absolute_commitments(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path)