from __future__ import annotations

from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.propositional_formula import PropositionalFormula


class Conjunction(PropositionalFormula):
    def __init__(self, arguments: list, is_self_standing=False):
        super().__init__(arguments=arguments, is_self_standing=is_self_standing)
    
    def get_tptp_axiom(self, bound_variables: list) -> str:
        tptp_axiom = self.bracketise(' & '.join([argument.get_tptp_axiom(bound_variables) for argument in self.arguments]))
        return tptp_axiom
    
    def to_cl(self) -> str:
        cl_axiom = '(' + 'and ' + ' '.join([argument.to_cl() for argument in self.arguments]) + ')'
        return cl_axiom
    
    def to_latex(self) -> str:
        latex_formula = r' \land '.join([argument.to_latex() for argument in self.arguments])
        return self.get_selfstanding_latex_if_needed(latex_formula=latex_formula)
    
    def __repr__(self):
        return Conjunction.bracketise(' and '.join([argument.__repr__() for argument in self.arguments]))

    def make_stronger(self, inverse_strength: bool) -> Formula:
        stronger_arguments = self.get_stronger_arguments(inverse_strength=inverse_strength)
        if inverse_strength:
            from objects.fol_logic.objects.disjunction import Disjunction
            return Disjunction(arguments=stronger_arguments, is_self_standing=self.is_self_standing)
        else:
            return Conjunction(arguments=stronger_arguments, is_self_standing=self.is_self_standing)