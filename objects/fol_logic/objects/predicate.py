from objects.fol_logic.objects.quantifying_formula import QuantifyingFormula, Quantifier
from objects.fol_logic.objects.symbol import Symbol
from objects.fol_logic.objects.variable import Variable


class Predicate(Symbol):
    registry = dict()
    
    def __init__(self, arity: int, origin_value=str(), tptp=str()):
        super().__init__(origin_value)
        self.arity = arity
        if len(tptp) > 0:
            self.tptp = tptp
        else:
            self.tptp = None
        Predicate.registry[origin_value] = self
        
    def to_tptp(self):
        if self.tptp:
            return self.tptp
        tptp_predicate = self.value.lower()
        tptp_predicate = Symbol.escape_tptp_chars(text=tptp_predicate)
        return tptp_predicate
    
    
    def to_cl(self) -> str:
        return self.value
    

    def create_instantiation(self):
        from objects.fol_logic.objects.atomic_formula import AtomicFormula
        variables = list()
        for index in range(self.arity):
            variable = Variable(letter=Variable.get_next_variable_letter())
            variables.append(variable)
        bound_variables = variables.copy()
        from objects.fol_logic.objects.identity import Identity
        if isinstance(self,Identity):
            from objects.fol_logic.objects.identity_formula import IdentityFormula
            quantified_formula = IdentityFormula(arguments=variables)
        else:
            quantified_formula = AtomicFormula(predicate=self, arguments=variables)
        instantiation = (
            QuantifyingFormula(
                quantified_formula=quantified_formula,
                bound_variables=bound_variables,
                quantifier=Quantifier.EXISTENTIAL,
                is_self_standing=True))
        return instantiation
    
ARITHMETIC_LESS_PREDICATE = Predicate(arity=2, tptp='$less', origin_value='<')
ARITHMETIC_GREATER_PREDICATE = Predicate(arity=2, tptp='$greater', origin_value='>')
ARITHMETIC_LESSEQ_PREDICATE = Predicate(arity=2, tptp='lesseq', origin_value='<=')
ARITHMETIC_GREATEREQ_PREDICATE = Predicate(arity=2, tptp='$greatereq', origin_value='>=')
