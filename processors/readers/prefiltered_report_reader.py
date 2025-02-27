import pandas


def get_prefiletered_non_commiting_predicates(prefiltered_non_relative_commitments_file_path: str) -> list:
    prefiletered_non_commiting_predicates_dataframe = (
        pandas.read_excel(
            prefiltered_non_relative_commitments_file_path))
    prefiletered_non_commiting_predicates_dataframe = (
        prefiletered_non_commiting_predicates_dataframe)[
            [
                'non-committing predicate',
                'non-committed predicate']
    ]
    prefiletered_non_commiting_predicates = (
        prefiletered_non_commiting_predicates_dataframe.values.tolist())
    
    return prefiletered_non_commiting_predicates
   