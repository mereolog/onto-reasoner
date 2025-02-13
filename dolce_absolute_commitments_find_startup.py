from processors.investigators.commitment_finders import find_absolute_commitments
from startup_commons import dolce_file_path, reasoner_artifacts_path

find_absolute_commitments(
    theory_file_path=dolce_file_path,
    reasoner_artifacts_path=reasoner_artifacts_path)