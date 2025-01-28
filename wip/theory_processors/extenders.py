from random import choice
from string import ascii_lowercase

from objects.fol_logic.objects.conjunction import Conjunction
from objects.fol_logic.objects.disjunction import Disjunction
from objects.fol_logic.objects.identity_formula import IdentityFormula
from objects.fol_logic import Negation
from objects.fol_logic.objects.quantifying_formula import QuantifyingFormula, Quantifier
from objects.fol_logic.objects.variable import Variable


def extend_theory_with_domain_size(theory: list, domain_size: int) -> list:
    extended_theory = theory.copy()
    terms_root = ''.join(choice(ascii_lowercase) for i in range(7))
    terms = list()
    
    for index in range(domain_size):
        terms.append(Variable(letter=terms_root+str(index)))
    diffs_conjuncts = list()
    for index1 in range(domain_size):
        for index2 in range(index1+1, domain_size):
            identity = IdentityFormula(arguments=[terms[index1], terms[index2]])
            diffs_conjuncts.append(Negation(arguments=[identity]))
    min_size_clause = Conjunction(arguments=diffs_conjuncts)
    extended_theory.append(min_size_clause)
    
    max_size_clause_all_bound_variable = Variable.get_next_variable()
    identity_disjuncts = list()
    for term in terms:
        identity = IdentityFormula(arguments=[max_size_clause_all_bound_variable, term])
        identity_disjuncts.append(identity)
    max_size_clause_consequent = Disjunction(arguments=identity_disjuncts)
    max_size_clause = (
        QuantifyingFormula(
            quantified_formula=max_size_clause_consequent,
            quantifier=Quantifier.UNIVERSAL, bound_variables=[max_size_clause_all_bound_variable]))
    extended_theory.append(max_size_clause)
    
    return extended_theory