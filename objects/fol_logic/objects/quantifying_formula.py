from __future__ import annotations

from enum import Enum

from objects.fol_logic.objects.formula import Formula


class Quantifier(Enum):
    UNIVERSAL = 'all'
    EXISTENTIAL = 'some'


class QuantifyingFormula(Formula):
    def __init__(self, quantified_formula: Formula, bound_variables: list, quantifier: Quantifier, is_self_standing=False):
        super().__init__(is_self_standing)
        self.quantified_formula = quantified_formula
        self.bound_variables = bound_variables
        self.quantifier = quantifier
        self.free_variables = self.__reset_free_variables()
        self.set_tptp_type()
    
    def __repr__(self):
        return ' '.join([self.quantifier.value, ','.join([variable.__repr__() for variable in self.bound_variables]),
                         self.quantified_formula.__repr__()])
    
    def get_tptp_axiom(self, bound_variables: set) -> str:
        if self.quantifier == Quantifier.UNIVERSAL:
            tptp_quantifier = '!'
        else:
            tptp_quantifier = '?'
        tptp_axiom = \
            ' '.join(
                [
                    tptp_quantifier,
                    '[', ','.join([variable.to_tptp() for variable in self.bound_variables]),
                    ']',
                    ':',
                    self.quantified_formula.get_tptp_axiom(bound_variables=list(bound_variables) + self.bound_variables)])
        return self.bracketise(tptp_axiom)
    
    def to_cl(self) -> str:
        if self.quantifier == Quantifier.UNIVERSAL:
            cl_quantifier = 'forall '
        else:
            cl_quantifier = 'exists '
        cl_axiom = \
            ''.join(
                [
                    cl_quantifier,
                    '(',
                    ' '.join([variable.to_cl() for variable in self.bound_variables]),
                    ')',
                    ' ',
                    self.quantified_formula.to_cl(),
                ])
        return self.bracketise(cl_axiom)
    
    def to_latex(self) -> str:
        if self.quantifier == Quantifier.UNIVERSAL:
            latex_quantifier = r'\forall'
        else:
            latex_quantifier = r'\exists'
        latex_formula = \
            ''.join(
                [
                    '(',
                    latex_quantifier,
                    ' ',
                    ','.join([variable.to_latex() for variable in self.bound_variables]),
                    '~',
                    ' ',
                    self.quantified_formula.to_latex(),
                    ')'
                ])
        return self.get_selfstanding_latex_if_needed(latex_formula=latex_formula)
    
    def __reset_free_variables(self):
        free_variables = set(self.quantified_formula.free_variables)
        for variable in self.bound_variables:
            if variable in free_variables:
                free_variables.remove(variable)
        return free_variables
    
    def set_tptp_type(self):
        self.tptp_type = self.quantified_formula.tptp_type
        
        
    def get_all_predicates(self) -> set:
        return self.quantified_formula.get_all_predicates()

    def make_stronger(self, inverse_strength: bool) -> Formula:
        if inverse_strength:
            if self.quantifier == Quantifier.UNIVERSAL:
                stronger_formula = (
                    QuantifyingFormula(
                        quantifier=Quantifier.EXISTENTIAL,
                        bound_variables=self.bound_variables,
                        is_self_standing=self.is_self_standing,
                        quantified_formula=self.quantified_formula.make_stronger(inverse_strength=inverse_strength)))
                return stronger_formula
            else:
                stronger_formula = (
                    QuantifyingFormula(
                        quantifier=Quantifier.EXISTENTIAL,
                        bound_variables=self.bound_variables,
                        is_self_standing=self.is_self_standing,
                        quantified_formula=self.quantified_formula.make_stronger(inverse_strength=inverse_strength)))
                return stronger_formula
        else:
            if self.quantifier == Quantifier.UNIVERSAL:
                stronger_formula = (
                    QuantifyingFormula(
                        quantifier=Quantifier.UNIVERSAL,
                        bound_variables=self.bound_variables,
                        is_self_standing=self.is_self_standing,
                        quantified_formula=self.quantified_formula.make_stronger(inverse_strength=inverse_strength)))
                return stronger_formula
            else:
                stronger_formula = (
                    QuantifyingFormula(
                        quantifier=Quantifier.UNIVERSAL,
                        bound_variables=self.bound_variables,
                        is_self_standing=self.is_self_standing,
                        quantified_formula=self.quantified_formula.make_stronger(inverse_strength=inverse_strength)))
                return stronger_formula