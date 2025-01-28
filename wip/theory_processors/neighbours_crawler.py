from objects.fol_logic.objects.formula import Formula


def find_neighbouring_supertheory(theory: list, main_theory: list) -> list:
    neighbouring_supertheory = set()
    for axiom in theory:
        neighbouring_supertheory = neighbouring_supertheory.union(find_neighbouring_axioms(focus_axiom=axiom,main_theory=main_theory))
    neighbouring_supertheory = list(neighbouring_supertheory)
    return neighbouring_supertheory

def find_neighbouring_axioms(focus_axiom: Formula, main_theory: list) -> set:
    neighbouring_axioms = set()
    focus_axiom_predicates = focus_axiom.get_all_predicates()
    for axiom in main_theory:
        axiom_predicates = axiom.get_all_predicates()
        if len(axiom_predicates.intersection(focus_axiom_predicates)) > 0:
            neighbouring_axioms.add(axiom)
    return neighbouring_axioms
