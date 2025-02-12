from __future__ import annotations

from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.propositional_formula import PropositionalFormula


class Equivalence(PropositionalFormula):
    def __init__(self, arguments: list, is_self_standing=False):
        if not len(arguments) == 2:
            raise Exception('Wrong equivalence initialisation')
        super().__init__(arguments=arguments, is_self_standing=is_self_standing)
        
    def get_tptp_axiom(self, bound_variables: list) -> str:
        tptp_axiom = self.bracketise(' '.join([self.arguments[0].get_tptp_axiom(bound_variables), '<=>', self.arguments[1].get_tptp_axiom(bound_variables)]))
        return tptp_axiom
        
    def to_cl(self) -> str:
        cl_axiom = '(' + 'iff ' + ' '.join([argument.to_cl() for argument in self.arguments]) + ')'
        return cl_axiom
    
    def to_latex(self) -> str:
        latex_formula = self.arguments[0].to_latex() + r' \equiv ' + self.arguments[1].to_latex()
        return self.get_selfstanding_latex_if_needed(latex_formula=latex_formula)
    
    def __repr__(self):
        return Equivalence.bracketise(self.arguments[0].__repr__() + ' iff ' + self.arguments[1].__repr__())

    def make_stronger(self, inverse_strength: bool) -> Formula:
        return self
    