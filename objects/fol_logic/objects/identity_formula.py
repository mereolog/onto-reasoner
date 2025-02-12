from __future__ import annotations

from objects.fol_logic.objects.atomic_formula import AtomicFormula
from objects.fol_logic.objects.identity import Identity


class IdentityFormula(AtomicFormula):
    def __init__(self, arguments: list, is_self_standing=False):
        super().__init__(predicate=Identity(), arguments=arguments, is_self_standing=is_self_standing)
        
    def get_tptp_axiom(self, bound_variables: list) -> str:
        tptp_arguments = self.get_tptp_variables(bound_variables=bound_variables)
        tptp_axiom = self.bracketise(formula=''.join([tptp_arguments[0], self.predicate.to_tptp(), tptp_arguments[1]]))
        return tptp_axiom
    
    def to_cl(self) -> str:
        cl_axiom = '(' + '=' + ' ' + ' '.join([argument.to_cl() for argument in self.arguments]) + ')'
        return cl_axiom
    
    def to_latex(self) -> str:
        latex_formula = self.arguments[0].to_latex() + r'=' + self.arguments[1].to_latex()
        return self.get_selfstanding_latex_if_needed(latex_formula=latex_formula)
    
    def __repr__(self):
        return ''.join([self.arguments[0].__repr__(), self.predicate.__repr__(), self.arguments[1].__repr__()])
    
