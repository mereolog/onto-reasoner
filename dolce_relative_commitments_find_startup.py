import pickle

from objects.commitments.relative_commitments import RelativeCommitments
from processors.investigators.commitment_finders import find_relative_commitments_using_grounds, \
    prefilter_out_relative_commitments
from processors.investigators.relative_commitment_filterer import filter_out_apparent_relative_commitments
from processors.investigators.subsumptions_finder import find_subsumptions
from processors.readers.prefiltered_report_reader import get_prefiletered_non_commiting_predicates
from startup_commons import dolce_file_path, reasoner_artifacts_path

prefilter_out_relative_commitments(
    theory_file_path=dolce_file_path,
    report_file_path='resources/outputs/reports/dolce_non-ri_report.xlsx',
    reasoner_artifacts_path=reasoner_artifacts_path)

prefiltered_non_commiting_predicates = (
    get_prefiletered_non_commiting_predicates(
        prefiltered_non_relative_commitments_file_path='resources/outputs/reports/dolce_non-ri_report.xlsx'))

find_relative_commitments_using_grounds(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path,
    report_file_path='dolce_ri_report.xlsx',
    skipped_predicate_couples=prefiltered_non_commiting_predicates)

pickle.dump(RelativeCommitments.registry, open('resources/outputs/pickles/dolce_all_relative_commitments.pickle', 'wb'))

dolce_subsumptions = (
    find_subsumptions(
        theory_file_path=dolce_file_path,
        reasoner_artifacts_path=reasoner_artifacts_path))

filter_out_apparent_relative_commitments(subsumptions=dolce_subsumptions)

pickle.dump(RelativeCommitments.registry, open('resources/outputs/pickles/dolce_genuine_only_relative_commitments.pickle', 'wb'))