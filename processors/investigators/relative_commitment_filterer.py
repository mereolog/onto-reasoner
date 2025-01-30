from objects.commitments.relative_commitments import RelativeCommitments


def filter_out_apparent_relative_commitments(subsumptions: list):
    relative_commitments = RelativeCommitments.registry.copy()
    
    for relative_commitment_1 in RelativeCommitments.registry:
        for relative_commitment_2 in RelativeCommitments.registry:
            if relative_commitment_1 == relative_commitment_2:
                continue
            if not relative_commitment_1.committing_predicate == relative_commitment_2.committing_predicate:
                continue
            commited_predicate_1 = relative_commitment_1.committed_predicate
            commited_predicate_2 = relative_commitment_2.committed_predicate
            if [commited_predicate_1, commited_predicate_2] in subsumptions:
                if relative_commitment_2 in relative_commitments:
                    relative_commitments.remove(relative_commitment_2)
                    print('Removing', relative_commitment_2.definition)
                    
    RelativeCommitments.registry = relative_commitments
    