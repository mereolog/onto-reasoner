from __future__ import annotations

import copy
import uuid

from objects.fol_logic.objects.variable import Variable


class Formula:
    registry = list()
    
    def __init__(self, is_self_standing=False, tptp_type='fof', comment: str = None):
        self.is_self_standing = is_self_standing
        self.tptp_type = tptp_type
        self.comment = comment
        self.free_variables = set()
        self.bound_variables = list()
        if is_self_standing:
            Formula.registry.append(self)
            
    def __lt__(self, other):
        if not isinstance(other, Formula):
            return NotImplemented
        return str(self).__lt__(str(other))
    
    def to_tptp(self) -> str:
        tptp_axiom = self.get_tptp_axiom(bound_variables=self.bound_variables)
        tptp_axiom = Formula.bracketise(tptp_axiom)
        tptp_formula = self.tptp_type + '(' + ' axiom' + str(uuid.uuid4()).replace('-', '') + ',' + 'axiom' + ',' + tptp_axiom + ')' + '.'
        return tptp_formula
    
    
    def to_cl(self) -> str:
        pass
    
    def to_latex(self) -> str:
        pass
    
    def get_selfstanding_latex_if_needed(self, latex_formula: str):
        if self.is_self_standing:
            return '$'+latex_formula+'$'
        else:
            return latex_formula
    
    def get_tptp_axiom(self, bound_variables: list) -> str:
        pass
    
    @staticmethod
    def bracketise(formula: str):
        return '(' + formula + ')'
    
    def replace_free_variable(self, old_variable: Variable, new_variable: Variable):
        for free_variable in self.free_variables:
            if free_variable == old_variable:
                self.replace_variable(old_variable=old_variable, new_variable=new_variable)
                
    def replace_variable(self, old_variable: Variable, new_variable: Variable):
        if hasattr(self, 'arguments'):
            for argument in self.arguments:
                argument.replace_variable(old_variable=old_variable, new_variable=new_variable)
    
    def copy(self):
        return copy.deepcopy(self)
    
    def set_tptp_type(self):
        pass
    
    def get_all_predicates(self) -> set:
        pass

    def make_stronger(self, inverse_strength: bool) -> Formula:
        pass