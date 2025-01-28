from __future__ import annotations

from objects.fol_logic.objects.equivalence import Equivalence
from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.propositional_formula import PropositionalFormula


class Implication(PropositionalFormula):
    def __init__(self, arguments: list, is_self_standing=False):
        if not len(arguments) == 2:
            raise Exception('Wrong implication initialisation')
        super().__init__(arguments=arguments, is_self_standing=is_self_standing)

    def get_tptp_axiom(self, bound_variables: list) -> str:
        tptp_axiom = self.bracketise(' '.join([self.arguments[0].get_tptp_axiom(bound_variables), '=>', self.arguments[1].get_tptp_axiom(bound_variables)]))
        return tptp_axiom
    
    def to_cl(self) -> str:
        cl_axiom = '(' + 'if' + ' ' + ' '.join([argument.to_cl() for argument in self.arguments]) + ')'
        return cl_axiom
        
    def __repr__(self):
        return Implication.bracketise('if ' + self.arguments[0].__repr__() + ' then ' + self.arguments[1].__repr__())


    def make_stronger(self, inverse_strength: bool) -> Formula:
        stronger_arguments = self.get_stronger_arguments(inverse_strength=inverse_strength)
        if inverse_strength:
            return Implication(arguments=self.arguments, is_self_standing=self.is_self_standing)
        else:
            return Equivalence(arguments=self.arguments, is_self_standing=self.is_self_standing)