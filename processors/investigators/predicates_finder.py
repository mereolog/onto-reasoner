from objects.fol_logic.objects.theory import Theory
from processors.readers.parsers.clif_parser import parse_clif


def find_n_ary_predicates(theory_file_path: str, arity: int) -> set:
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = parse_clif(cl_theory_text)
    cl_theory = Theory(parts=cl_theory_axioms)
    n_ary_predicates = set(cl_theory.get_n_ary_predicates_map()[arity])
    return n_ary_predicates


def find_all_predicates(theory_file_path: str) -> set:
    all_predicates = set()
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = parse_clif(cl_theory_text)
    cl_theory = Theory(parts=cl_theory_axioms)
    n_ary_predicates_map = cl_theory.get_n_ary_predicates_map()
    for arity, predicates in n_ary_predicates_map.items():
        all_predicates = all_predicates.union(predicates)
    return all_predicates


def calculate_theory_signature_count(theory_file_path: str) -> dict:
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = parse_clif(cl_theory_text)
    cl_theory = Theory(parts=cl_theory_axioms)
    theory_signature_count = dict()
    arity = 1
    while True:
        if arity in cl_theory.get_n_ary_predicates_map():
            n_ary_predicates = set(cl_theory.get_n_ary_predicates_map()[arity])
        else:
            break
        theory_signature_count[arity] = len(n_ary_predicates)
        arity += 1
    return theory_signature_count
    
    