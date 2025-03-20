from objects.fol_logic.objects.term import Term


class FunctionSymbol(Term):
    registry = dict()
    
    def __init__(self, term: Term, arguments: list, origin_value=str(), tptp=str()):
        Term.__init__(self, origin_value)
        self.term = term
        self.arguments = arguments
        if len(tptp) > 0:
            self.tptp = tptp
        else:
            self.tptp = None
        FunctionSymbol.registry[origin_value] = self
        
    
