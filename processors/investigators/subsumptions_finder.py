from tqdm import tqdm

from objects.fol_logic.objects.atomic_formula import AtomicFormula
from objects.fol_logic.objects.implication import Implication
from objects.fol_logic.objects.negation import Negation
from objects.fol_logic.objects.quantifying_formula import QuantifyingFormula, Quantifier
from objects.fol_logic.objects.theory import Theory
from objects.fol_logic.objects.variable import Variable
from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from processors.reasoners.consistency_result import ProverResult
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from wip.theory_processors.helpers import get_theory_id

def find_subsumptions(
        theory_file_path: str,
        reasoner_artifacts_path: str) -> list:
    subsumptions = list()
    
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = extended_parse_clif(cl_theory_text)
    cl_theory = Theory(parts=cl_theory_axioms)
    unary_predicates = set(cl_theory.get_n_ary_predicates_map()[1])
    
    for unary_predicate_1 in tqdm(unary_predicates, position=0, desc='checked potentially subsumed predicates'):
        for unary_predicate_2 in unary_predicates:
            if unary_predicate_1 == unary_predicate_2:
                continue
            extended_cl_theory_axioms = cl_theory_axioms.copy()
            variable = Variable.get_next_variable()
            atomic_formula_1 = AtomicFormula(predicate=unary_predicate_1, arguments=[variable])
            atomic_formula_2 = AtomicFormula(predicate=unary_predicate_2, arguments=[variable])
            subsumption_formula = (
                QuantifyingFormula(
                    quantified_formula=Implication(arguments=[atomic_formula_1, atomic_formula_2]),
                    bound_variables=[variable],
                    quantifier=Quantifier.UNIVERSAL))
            extended_cl_theory_axioms.append(Negation(arguments=[subsumption_formula]))
            extended_theory_id = get_theory_id(theory=extended_cl_theory_axioms)
            vampire_input_file_path = reasoner_artifacts_path + extended_theory_id + '.tptp'
            vampire_output_file_path = reasoner_artifacts_path + extended_theory_id + '.szs'
            with open(file=vampire_input_file_path, mode='w') as tptp_file:
                for axiom in extended_cl_theory_axioms:
                    axiom.is_self_standing = True
                    tptp_file.write(axiom.to_tptp())
                    tptp_file.write('\n')
            result, time = (
                decide_whether_theory_is_consistent(
                    vampire_input_file_path=vampire_input_file_path,
                    vampire_output_file_path=vampire_output_file_path))
            if result == ProverResult.INCONSISTENT:
                subsumptions.append([unary_predicate_1, unary_predicate_2])
            if result == ProverResult.UNDECIDED:
                print('I was unable to decide whether', str(unary_predicate_2), 'subsumes', str(unary_predicate_1), '- I spent',
                      str(time), 'seconds on this.')
    return subsumptions


def find_subsumption_leaf_predicates(
        theory_file_path: str,
        reasoner_artifacts_path: str) -> set:
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = extended_parse_clif(cl_theory_text)
    cl_theory = Theory(parts=cl_theory_axioms)
    unary_predicates = set(cl_theory.get_n_ary_predicates_map()[1])
    subsumption_leaf_predicates = unary_predicates.copy()
    
    subsumptions = (
        find_subsumptions(
            theory_file_path=theory_file_path,
            reasoner_artifacts_path=reasoner_artifacts_path))
    
    for subsumption in subsumptions:
        if subsumption[2] in subsumption_leaf_predicates:
            subsumption_leaf_predicates.remove(subsumption[2])
    
    return subsumption_leaf_predicates