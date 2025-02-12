from objects.commitments.relative_commitments import RelativeCommitments


def filter_out_apparent_relative_commitments(subsumptions: list):
    filtered_relative_commitments = RelativeCommitments.registry.copy()
    
    for relative_commitment_1 in RelativeCommitments.registry:
        for relative_commitment_2 in RelativeCommitments.registry:
            if relative_commitment_1 == relative_commitment_2:
                continue
            if __relative_commitment_1_can_be_reduced_to_relative_commitment_2(relative_commitment_1=relative_commitment_1, relative_commitment_2=relative_commitment_2, subsumptions=subsumptions):
                if relative_commitment_1 in filtered_relative_commitments:
                    filtered_relative_commitments.remove(relative_commitment_1)
                    # print('Filtering out', relative_commitment_1.definition, 'because of', relative_commitment_2.definition)
                    break
                    
    RelativeCommitments.registry = filtered_relative_commitments
    for relative_commitment in filtered_relative_commitments:
        print('Retained', relative_commitment.definition)
    
    
def __relative_commitment_1_can_be_reduced_to_relative_commitment_2(
        relative_commitment_1: RelativeCommitments,
        relative_commitment_2: RelativeCommitments,
        subsumptions: list) -> bool:
    if relative_commitment_1.committing_predicate == relative_commitment_2.committing_predicate and relative_commitment_1.committed_predicate == relative_commitment_2.committed_predicate:
        return False
    if relative_commitment_1.committing_predicate == relative_commitment_2.committing_predicate and [relative_commitment_2.committed_predicate, relative_commitment_1.committed_predicate] in subsumptions:
        return True
    # if relative_commitment_2.committed_predicate == relative_commitment_1.committed_predicate and [relative_commitment_1.committing_predicate, relative_commitment_2.committing_predicate] in subsumptions:
    #     return True
    # if [relative_commitment_2.committed_predicate, relative_commitment_1.committed_predicate] in subsumptions and [relative_commitment_1.committing_predicate, relative_commitment_2.committing_predicate] in subsumptions:
    #     return True
    return False


# def __relative_commitment_1_can_be_reduced_to_relative_commitment_2(
#         relative_commitment_1: RelativeCommitments,
#         relative_commitment_2: RelativeCommitments,
#         subsumptions: list) -> bool:
#     if relative_commitment_1.committing_predicate == relative_commitment_2.committing_predicate and relative_commitment_1.committed_predicate == relative_commitment_2.committed_predicate:
#         return False
#     if relative_commitment_2.committing_predicate == relative_commitment_1.committing_predicate and [relative_commitment_2.committed_predicate, relative_commitment_1.committed_predicate] in subsumptions:
#         return True
#     if relative_commitment_2.committed_predicate == relative_commitment_1.committed_predicate and [relative_commitment_1.committing_predicate, relative_commitment_2.committing_predicate] in subsumptions:
#         return True
#     if [relative_commitment_2.committed_predicate, relative_commitment_1.committed_predicate] in subsumptions and [relative_commitment_1.committing_predicate, relative_commitment_2.committing_predicate] in subsumptions:
#         return True
#     return False
#