from objects.fol_logic.objects.atomic_formula import AtomicFormula
from objects.fol_logic.objects.term import Term


class FunctionSymbol(Term, AtomicFormula):
    registry = dict()
    
    def __init__(self, term: Term, arguments: list, origin_value=str(), tptp=str()):
        Term.__init__(self, origin_value)
        AtomicFormula.__init__(self, predicate=term,arguments=arguments)
        if len(tptp) > 0:
            self.tptp = tptp
        else:
            self.tptp = None
        FunctionSymbol.registry[origin_value] = self
        
    
