import pickle

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.relative_commitment_filterer import filter_out_apparent_relative_commitments
from processors.investigators.subsumptions_finder import find_subsumptions
from startup_commons import dolce_file_path, reasoner_artifacts_path

dolce_subsumptions = (
    find_subsumptions(
        theory_file_path=dolce_file_path,
        reasoner_artifacts_path=reasoner_artifacts_path))

RelativeCommitments.registry = pickle.load(open('resources/outputs/pickles/dolce_all_relative_commitments.pickle', 'rb'))

filter_out_apparent_relative_commitments(subsumptions=dolce_subsumptions)

pickle.dump(RelativeCommitments.registry, open('resources/outputs/pickles/dolce_genuine_only_relative_commitments.pickle', 'wb'))


