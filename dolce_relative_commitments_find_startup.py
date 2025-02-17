import logging
import pickle

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.commitment_finders import find_relative_commitments_using_grounds, \
    find_remaining_relative_commitments_without_grounds
from processors.investigators.subsumptions_finder import find_subsumptions
from startup_commons import dolce_file_path, reasoner_artifacts_path

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p', filename='dolce_ri_log.log')


dolce_subsumptions = (
    find_subsumptions(
        theory_file_path=dolce_file_path,
        reasoner_artifacts_path=reasoner_artifacts_path))

find_relative_commitments_using_grounds(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path,
    report_file_path='dolce_ri_report.xlsx')

pickle.dump(RelativeCommitments.registry, open('resources/outputs/dolce_all_relative_commitments.pickle', 'wb'))

find_remaining_relative_commitments_without_grounds(
    relative_commitments_with_ground_report_file_path='dolce_ri_report.xlsx',
    reasoner_artifacts_path=reasoner_artifacts_path,
    report_file_path='extended_dolce_ri_report.xlsx',
    theory_file_path=dolce_file_path)

pickle.dump(RelativeCommitments.registry, open('resources/outputs/dolce_all_plus_relative_commitments.pickle', 'wb'))

