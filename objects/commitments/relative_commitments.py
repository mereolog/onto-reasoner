from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.predicate import Predicate


class RelativeCommitments:
    registry = set()
    
    def __init__(
            self,
            committing_predicate: Predicate,
            committed_predicate: Predicate,
            ground: Predicate,
            definition: Formula,
            evidence_id: str):
        self.committing_predicate = committing_predicate
        self.committed_predicate = committed_predicate
        self.ground = ground
        self.definition = definition
        self.evidence_id = evidence_id
        
        RelativeCommitments.registry.add(self)
        
    def __repr__(self):
        return 'Predicate ' + self.committing_predicate + ' commits to ' + self.committed_predicate + ' because of ' + self.definition
    
    def __str__(self):
        return 'Predicate ' + self.committing_predicate + ' commits to ' + self.committed_predicate + ' because of ' + self.definition
