import logging
import pickle
import sys

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.commitment_finders import find_relative_commitments_using_grounds, \
    find_remaining_relative_commitments_without_grounds, prefilter_out_relative_commitments
from processors.investigators.predicates_finder import calculate_theory_signature_count
from processors.investigators.subsumptions_finder import find_subsumptions
from processors.readers.prefiltered_report_reader import get_prefiletered_non_commiting_predicates
from startup_commons import dolce_file_path, reasoner_artifacts_path

# theory_signature_count = calculate_theory_signature_count(theory_file_path=dolce_file_path)
# print(theory_signature_count)

prefilter_out_relative_commitments(
    theory_file_path=dolce_file_path,
    report_file_path='resources/outputs/reports/dolce_non-ri_report.xlsx',
    reasoner_artifacts_path=reasoner_artifacts_path)

prefiletered_non_commiting_predicates = (
    get_prefiletered_non_commiting_predicates(
        prefiltered_non_relative_commitments_file_path='resources/outputs/reports/dolce_non-ri_report.xlsx'))


find_relative_commitments_using_grounds(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path,
    report_file_path='dolce_ri_report.xlsx',
    skipped_predicate_couples=prefiletered_non_commiting_predicates)

pickle.dump(RelativeCommitments.registry, open('resources/outputs/pickles/dolce_all_relative_commitments.pickle', 'wb'))

find_remaining_relative_commitments_without_grounds(
    relative_commitments_with_ground_report_file_path='resources/outputs/reports/dolce_ri_report.xlsx',
    reasoner_artifacts_path=reasoner_artifacts_path,
    report_file_path='resources/outputs/reports/extended_dolce_ri_report.xlsx',
    theory_file_path=dolce_file_path)

pickle.dump(RelativeCommitments.registry, open('resources/outputs/pickles/dolce_all_plus_relative_commitments.pickle', 'wb'))

