import sys

import networkx
import matplotlib.pyplot as plt
import pickle

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.commitment_finders import find_relative_commitments
from processors.investigators.relative_commitment_filterer import filter_out_apparent_relative_commitments
from processors.investigators.subsumptions_finder import find_subsumption_leaf_predicates, find_subsumptions

dolce_file_path='resources/midputs/dolce.cl'
reasoner_artifacts_path='resources/midputs/reasoner_artifacts/'

find_relative_commitments(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path)

dolce_subsumptions = (
    find_subsumptions(
        theory_file_path=dolce_file_path,
        reasoner_artifacts_path=reasoner_artifacts_path))

filter_out_apparent_relative_commitments(subsumptions=dolce_subsumptions)



pickle.dump(RelativeCommitments.registry, open('relative_commitments.pickle', 'wb'))
