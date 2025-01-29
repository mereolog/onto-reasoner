from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.predicate import Predicate


class RelativeCommitments:
    registry = set()
    
    def __init__(
            self,
            committing_predicate: Predicate,
            committed_predicate: Predicate,
            definition: Formula):
        self.committing_predicate = committing_predicate
        self.committed_predicate = committed_predicate
        self.definition = definition
        
        RelativeCommitments.registry.add(self)
        