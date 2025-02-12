from __future__ import annotations

from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.propositional_formula import PropositionalFormula


class Negation(PropositionalFormula):
    def __init__(self, arguments: list, is_self_standing=False):
        if not len(arguments) == 1:
            raise Exception('Wrong negation initialisation')
        super().__init__(arguments=arguments, is_self_standing=is_self_standing)

    def __repr__(self):
        return 'not' + Negation.bracketise(self.arguments[0].__repr__())
        
    def get_tptp_axiom(self, bound_variables: list) -> str:
        tptp_axiom = self.bracketise('~' + self.arguments[0].get_tptp_axiom(bound_variables))
        return tptp_axiom
    
    def to_cl(self) -> str:
        cl_axiom = '(' + 'not ' + ' '.join([argument.to_cl() for argument in self.arguments]) + ')'
        return cl_axiom
    
    def to_latex(self) -> str:
        latex_formula = r'\neg ' + self.arguments[0].to_latex()
        return self.get_selfstanding_latex_if_needed(latex_formula=latex_formula)


    def make_stronger(self, inverse_strength: bool) -> Formula:
        stronger_arguments = self.get_stronger_arguments(inverse_strength=not inverse_strength)
        return Negation(arguments=stronger_arguments, is_self_standing=self.is_self_standing)
    