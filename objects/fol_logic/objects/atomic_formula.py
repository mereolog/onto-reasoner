from __future__ import annotations

import logging
from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.predicate import Predicate
from objects.fol_logic.objects.term import Term
from objects.fol_logic.objects.variable import Variable


class AtomicFormula(Formula):
    
    def __init__(self, predicate: Predicate, arguments: list, is_self_standing=False, tptp_type='fof', origin_type=str):
        super().__init__(is_self_standing, tptp_type=tptp_type)
        self.predicate = predicate
        self.arguments = arguments
        self.origin_type = origin_type
        self.__set_free_variables()
        self.set_tptp_type()
            
    def __repr__(self):
        return ''.join([self.predicate.__repr__(), '(', ','.join([argument.__repr__() for argument in self.arguments]), ')'])
        
    def __set_free_variables(self):
        for argument in self.arguments:
            if isinstance(argument, Variable):
                self.free_variables.add(argument)
    
    def swap_arguments(self, inplace=False):
        if inplace:
            self.arguments.reverse()
        else:
            reversed_arguments = self.arguments.copy()
            reversed_arguments.reverse()
            return AtomicFormula(predicate=self.predicate, arguments=reversed_arguments)
            
    def replace_arguments(self, arguments: list, inplace=False):
        if inplace:
            self.arguments = arguments
        else:
            return AtomicFormula(predicate=self.predicate, arguments=arguments, is_self_standing=self.is_self_standing)
        
    def replace_argument(self, argument: Term, index: int, inplace=False):
        if index > len(self.arguments):
            logging.error(msg='Index out of bounds for argument replacement')
            return
        replaced_arguments = self.arguments.copy()
        replaced_arguments[index] = argument
        if inplace:
            self.arguments = replaced_arguments
        else:
            return AtomicFormula(predicate=self.predicate, arguments=replaced_arguments, is_self_standing=self.is_self_standing)
        
        
    def get_tptp_variables(self, bound_variables: list) -> list:
        tptp_arguments = list()
        for argument in self.arguments:
            if argument in bound_variables:
                use_as_constant = False
            else:
                use_as_constant = True
            tptp_arguments.append(argument.to_tptp(use_as_constant))
        return tptp_arguments


    def get_tptp_axiom(self, bound_variables: list) -> str:
        tptp_arguments = self.get_tptp_variables(bound_variables=bound_variables)
        tptp_axiom = self.predicate.to_tptp() + '(' + ','.join(tptp_arguments) + ')'
        return tptp_axiom
    
    
    def to_cl(self) -> str:
        cl_axiom = '(' + self.predicate.to_cl() + ' ' + ' '.join([argument.to_cl() for argument in self.arguments]) + ')'
        return cl_axiom
    
    def replace_variable(self, old_variable: Variable, new_variable: Variable):
        arguments_copy = self.arguments.copy()
        for index in range(len(self.arguments)):
            if self.arguments[index] == old_variable:
                arguments_copy[index] = new_variable
        self.arguments = arguments_copy
        
    def set_tptp_type(self):
        for argument in self.arguments:
            if not argument.origin_type == str:
                self.tptp_type = 'tff'
                return
        
    
    def get_all_predicates(self) -> set:
        return {self.predicate}


    def make_stronger(self, inverse_strength: bool) -> Formula:
        return self