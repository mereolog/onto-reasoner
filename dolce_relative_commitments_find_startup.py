import pickle

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.commitment_finders import find_relative_commitments
from processors.investigators.subsumptions_finder import find_subsumptions
from startup_commons import dolce_file_path, reasoner_artifacts_path

dolce_subsumptions = (
    find_subsumptions(
        theory_file_path=dolce_file_path,
        reasoner_artifacts_path=reasoner_artifacts_path))

find_relative_commitments(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path,
    report_file_path='dolce_ri_report.xlsx')

pickle.dump(RelativeCommitments.registry, open('resources/outputs/dolce_all_relative_commitments.pickle', 'wb'))
