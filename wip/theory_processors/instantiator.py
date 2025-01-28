from processors.readers.parsers.clif_parser import parse_clif


def instantiate_cl_theory(cl_theory_file_path: str, instantiated_cl_theory_file_path: str, cl_theory: list = None):
    if not cl_theory:
        with open(cl_theory_file_path) as cl_theory_file:
            cl_theory_text = cl_theory_file.read()
        cl_theory = parse_clif(cl_theory_text)
    predicates = set()
    for axiom in cl_theory:
        axiom_predicates = axiom.get_all_predicates()
        predicates = predicates.union(axiom_predicates)
    instantiated_cl_theory = cl_theory.copy()
    for predicate in predicates:
        instantiated_cl_theory.append(predicate.create_instantiation())
    cl_theory_text = str()
    for axiom in instantiated_cl_theory:
        cl_theory_text += str(axiom.to_cl())
        cl_theory_text += '\n'
    with open(instantiated_cl_theory_file_path, mode='w') as cl_instantiated_theory_file:
        cl_instantiated_theory_file.write(cl_theory_text)