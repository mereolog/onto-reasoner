from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.indiscourse import Indiscourse
from objects.fol_logic.objects.outdiscourse import Outdiscourse


class Theory:
    def __init__(self, parts, title: str = None, comment: str = None):
        self.parts = parts
        self.formulae = parts.copy()
        self.outdiscourse = None
        self.indiscourse = None
        self.__set_discourses()
        self.title = title
        self.comment = comment
        
    def __set_discourses(self):
        for part in self.parts:
            if isinstance(part, Indiscourse):
                self.indiscourse = part
                if isinstance(self.formulae, list):
                    self.formulae.remove(part)
            if isinstance(part, Outdiscourse):
                self.outdiscourse = part
                if isinstance(self.formulae, list):
                    self.formulae.remove(part)
                    
    def get_n_ary_predicates_map(self) -> dict:
        n_ary_predicates_map = dict()
        for formula in self.formulae:
            if isinstance(formula, Formula):
                formula_predicates = formula.get_all_predicates()
                for formula_predicate in formula_predicates:
                    if formula_predicate.arity in n_ary_predicates_map:
                        n_ary_predicates = n_ary_predicates_map[formula_predicate.arity]
                    else:
                        n_ary_predicates = set()
                        n_ary_predicates_map[formula_predicate.arity] = n_ary_predicates
                    n_ary_predicates.add(formula_predicate)
        return n_ary_predicates_map