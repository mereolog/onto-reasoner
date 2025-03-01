import pandas
from tqdm import tqdm

from objects.commitments.relative_commitments import RelativeCommitments
from objects.fol_logic.objects.atomic_formula import AtomicFormula
from objects.fol_logic.objects.conjunction import Conjunction
from objects.fol_logic.objects.identity import Identity
from objects.fol_logic.objects.identity_formula import IdentityFormula
from objects.fol_logic.objects.implication import Implication
from objects.fol_logic.objects.negation import Negation
from objects.fol_logic.objects.predicate import Predicate
from objects.fol_logic.objects.quantifying_formula import QuantifyingFormula, Quantifier
from objects.fol_logic.objects.variable import Variable
from processors.investigators.predicates_finder import find_n_ary_predicates, find_all_predicates
from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from processors.reasoners.consistency_result import ProverResult
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from wip.theory_processors.helpers import get_theory_id


def find_absolute_commitments(theory_file_path: str, reasoner_artifacts_path: str):
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = extended_parse_clif(cl_theory_text)
    unary_predicates = find_n_ary_predicates(theory_file_path=theory_file_path, arity=1)
    
    __iterate_through_predicates_in_search_for_absolute_commitments(
        unary_predicates=unary_predicates,
        cl_theory_axioms=cl_theory_axioms,
        reasoner_artifacts_path=reasoner_artifacts_path)


def find_relative_commitments_using_grounds(
        theory_file_path: str,
        reasoner_artifacts_path: str,
        report_file_path: str,
        skipped_predicate_couples: list = None):
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = extended_parse_clif(cl_theory_text)
    
    unary_predicates = find_n_ary_predicates(theory_file_path=theory_file_path, arity=1)
    all_predicates = find_all_predicates(theory_file_path=theory_file_path)
    non_unary_predicates = all_predicates.difference(unary_predicates)
    
    __iterate_through_predicates_in_search_for_relative_commitments(
        unary_predicates=unary_predicates,
        non_unary_predicates=non_unary_predicates,
        reasoner_artifacts_path=reasoner_artifacts_path,
        cl_theory_axioms=cl_theory_axioms,
        report_file_path=report_file_path,
        skipped_predicate_couples=skipped_predicate_couples)


def find_remaining_relative_commitments_without_grounds(
        reasoner_artifacts_path: str,
        relative_commitments_with_ground_report_file_path: str,
        theory_file_path: str,
        report_file_path: str):
    report_dict = dict()
    report_count = 0
    Variable.clear_used_variable_letters()
    
    report = pandas.read_excel(relative_commitments_with_ground_report_file_path)
    truncated_report = report.copy()
    truncated_report = truncated_report[['committing predicate','committed predicate', 'is relative commitment']]
    undecided_cases = truncated_report[truncated_report['is relative commitment'].isnull()]
    undecided_cases.drop_duplicates(inplace=True)
    
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = extended_parse_clif(cl_theory_text)
    
    for undecided_case_tuple in undecided_cases.itertuples():
        commiting_predicate_string = undecided_case_tuple[1]
        commited_predicate_string = undecided_case_tuple[2]
        variable_1 = Variable.get_next_variable()
        variable_2 = Variable.get_next_variable()
        commiting_predicate = Predicate(arity=1, origin_value=commiting_predicate_string)
        commited_predicate = Predicate(arity=1, origin_value=commited_predicate_string)
        committing_formula = (
            QuantifyingFormula(
                quantified_formula=AtomicFormula(predicate=commiting_predicate, arguments=[variable_1]),
                bound_variables=[variable_1],
                quantifier=Quantifier.EXISTENTIAL))
        committed_formula = (
            QuantifyingFormula(
                quantified_formula=AtomicFormula(predicate=commited_predicate,arguments=[variable_2]),
                bound_variables=[variable_2],
                quantifier=Quantifier.EXISTENTIAL))
        relative_commitment_definition = Implication(arguments=[committing_formula, committed_formula])
        negation_relative_commitment_definition = Negation(arguments=[relative_commitment_definition])
        extended_cl_theory_axioms = cl_theory_axioms.copy()
        extended_cl_theory_axioms.append(negation_relative_commitment_definition)
        
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
                vampire_output_file_path=vampire_output_file_path,
                time=60))
        is_relative_commitment = False
        if result == ProverResult.INCONSISTENT:
            RelativeCommitments(committing_predicate=commiting_predicate,
                                committed_predicate=commited_predicate,
                                ground=None,
                                definition=relative_commitment_definition,
                                evidence_id=extended_theory_id)
            is_relative_commitment = True
        if result == ProverResult.UNDECIDED:
            print('I was not able to ascertain whether',
                  str(commiting_predicate),
                  'commits to',
                  str(commited_predicate),
                  'using',
                  str(relative_commitment_definition),
                  'See:', extended_theory_id)
            is_relative_commitment = None
        relative_commitment_definition.is_self_standing = True
        report = \
            {
                'committing predicate': commiting_predicate,
                'committed predicate': commited_predicate,
                'ground': None,
                'is relative commitment': is_relative_commitment,
                'definition': '$$',
                'evidence_id': extended_theory_id,
                'elapsed time': str(time),
                'committing predicate in LaTeX': commiting_predicate.to_latex(True),
                'committed predicate  in LaTeX': commited_predicate.to_latex(True),
                'ground in LaTeX': '$$',
                'definition in LaTeX': '$$',
            }
        report_dict[report_count] = report
        report_count += 1
        report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
        report_dataframe.to_excel(report_file_path, index=False)


def prefilter_out_relative_commitments(
        reasoner_artifacts_path: str,
        theory_file_path: str,
        report_file_path: str):
    report_dict = dict()
    report_count = 0
    Variable.clear_used_variable_letters()
    
    with open(theory_file_path) as cl_theory_file:
        cl_theory_text = cl_theory_file.read()
    cl_theory_axioms = extended_parse_clif(cl_theory_text)
    unary_predicates = find_n_ary_predicates(theory_file_path=theory_file_path, arity=1)
    for unary_predicate1 in unary_predicates:
        for unary_predicate2 in unary_predicates:
            if unary_predicate1 == unary_predicate2:
                continue
            variable_1 = Variable.get_next_variable()
            variable_2 = Variable.get_next_variable()
            committing_formula = (
                QuantifyingFormula(
                    quantified_formula=AtomicFormula(predicate=unary_predicate1, arguments=[variable_1]),
                    bound_variables=[variable_1],
                    quantifier=Quantifier.EXISTENTIAL))
            committed_formula = (
                QuantifyingFormula(
                    quantified_formula=AtomicFormula(predicate=unary_predicate2, arguments=[variable_2]),
                    bound_variables=[variable_2],
                    quantifier=Quantifier.EXISTENTIAL))
            relative_commitment_definition = Implication(arguments=[committing_formula, committed_formula])
            negation_relative_commitment_definition = Negation(arguments=[relative_commitment_definition])
            extended_cl_theory_axioms = cl_theory_axioms.copy()
            extended_cl_theory_axioms.append(negation_relative_commitment_definition)
            
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
                    vampire_output_file_path=vampire_output_file_path,
                    time=600))
            if result == ProverResult.CONSISTENT:
                report = \
                    {
                        'non-committing predicate': unary_predicate1,
                        'non-committed predicate': unary_predicate2,
                        'elapsed time': str(time),
                        'non-committing predicate in LaTeX': unary_predicate1.to_latex(True),
                        'non-committed predicate  in LaTeX': unary_predicate2.to_latex(True),
                    }
                report_dict[report_count] = report
                report_count += 1
                if report_count % 100 == 0:
                    report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
                    report_dataframe.to_excel(report_file_path, index=False)
    
    report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
    report_dataframe.to_excel(report_file_path, index=False)

def __iterate_through_predicates_in_search_for_relative_commitments(
        unary_predicates: set,
        non_unary_predicates: set,
        skipped_predicate_couples: list,
        cl_theory_axioms: list,
        reasoner_artifacts_path: str,
        report_file_path: str):
    report_dict = dict()
    report_count = 0
    for unary_predicate1 in unary_predicates:
        for unary_predicate2 in unary_predicates:
            if unary_predicate1 == unary_predicate2:
                continue
            for n_ary_predicate in non_unary_predicates:
                if isinstance(n_ary_predicate, Identity):
                    continue
                if [str(unary_predicate1), str(unary_predicate2)] in skipped_predicate_couples:
                    continue
                for index in range(n_ary_predicate.arity):
                    Variable.clear_used_variable_letters()
                    prevariables = list()
                    for preindex in range(index):
                        prevariable = Variable.get_next_variable()
                        prevariables.append(prevariable)
                    variable_1 = Variable.get_next_variable()
                    postvariables = list()
                    for postindex in range(index + 1, n_ary_predicate.arity):
                        postvariable = Variable.get_next_variable()
                        postvariables.append(postvariable)
                    unary_predicate_1_subformula = AtomicFormula(predicate=unary_predicate1, arguments=[variable_1])
                    for variable in prevariables + [variable_1] + postvariables:
                        if not variable == variable_1:
                            unary_predicate_2_subsubformula = (
                                AtomicFormula(
                                    predicate=unary_predicate2,
                                    arguments=[variable]))
                            diff_subsubformula = Negation(arguments=[IdentityFormula(arguments=[variable_1, variable])])
                            n_ary_predicate_subsubformula = (
                                AtomicFormula(
                                    predicate=n_ary_predicate,
                                     arguments=prevariables + [variable_1] + postvariables))
                            unary_predicate_2_subformula = (
                                QuantifyingFormula(
                                    quantified_formula=Conjunction(arguments=[n_ary_predicate_subsubformula, unary_predicate_2_subsubformula,diff_subsubformula]),
                                    bound_variables=prevariables + postvariables,
                                    quantifier=Quantifier.EXISTENTIAL))
                            relative_commitment_definition = (
                                QuantifyingFormula(
                                    quantified_formula=Implication(arguments=[unary_predicate_1_subformula, unary_predicate_2_subformula]),
                                    bound_variables=[variable_1],
                                    quantifier=Quantifier.UNIVERSAL))
                            negation_relative_commitment_definition = Negation(
                                arguments=[relative_commitment_definition])
                            extended_cl_theory_axioms = cl_theory_axioms.copy()
                            extended_cl_theory_axioms.append(negation_relative_commitment_definition)
                            
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
                                    vampire_output_file_path=vampire_output_file_path,
                                    time=1800))
                            is_relative_commitment = False
                            if result == ProverResult.INCONSISTENT:
                                RelativeCommitments(committing_predicate=unary_predicate1,
                                                    committed_predicate=unary_predicate2,
                                                    ground=n_ary_predicate,
                                                    definition=relative_commitment_definition,
                                                    evidence_id=extended_theory_id)
                                is_relative_commitment = True
                            if result == ProverResult.UNDECIDED:
                                print('I was not able to ascertain whether',
                                      str(unary_predicate1),
                                      'commits to',
                                      str(unary_predicate2),
                                      'using',
                                      str(relative_commitment_definition),
                                      'See:', extended_theory_id)
                                is_relative_commitment = None
                            relative_commitment_definition.is_self_standing = True
                            report = \
                                {
                                    'committing predicate': unary_predicate1,
                                    'committed predicate': unary_predicate2,
                                    'ground': n_ary_predicate,
                                    'is relative commitment': is_relative_commitment,
                                    'definition': relative_commitment_definition,
                                    'evidence_id': extended_theory_id,
                                    'elapsed time': str(time),
                                    'committing predicate in LaTeX': unary_predicate1.to_latex(True),
                                    'committed predicate  in LaTeX': unary_predicate2.to_latex(True),
                                    'ground in LaTeX': n_ary_predicate.to_latex(True),
                                    'definition in LaTeX': relative_commitment_definition.to_latex(),
                                }
                            report_dict[report_count] = report
                            report_count += 1
                            if report_count % 10000 == 0:
                                report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
                                report_dataframe.to_excel(report_file_path, index=False)
    
    report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
    report_dataframe.to_excel(report_file_path, index=False)

def __iterate_through_predicates_in_search_for_absolute_commitments(
        unary_predicates: set,
        cl_theory_axioms: list,
        reasoner_artifacts_path: str):
    for unary_predicate in tqdm(unary_predicates, desc='checked predicates'):
        extended_cl_theory_axioms = cl_theory_axioms.copy()
        variable = Variable.get_next_variable()
        atomic_formula = AtomicFormula(predicate=unary_predicate, arguments=[variable])
        existential_formula = (
            QuantifyingFormula(
                quantified_formula=atomic_formula,
                bound_variables=[variable],
                quantifier=Quantifier.EXISTENTIAL))
        extended_cl_theory_axioms.append(Negation(arguments=[existential_formula]))
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
                vampire_output_file_path=vampire_output_file_path,
                time=0))
        if result == ProverResult.INCONSISTENT:
            print('Predicate', str(unary_predicate), 'is found as commiting.')
        if result == ProverResult.UNDECIDED:
            print(
                'I was not able to ascertain whether the theory commits to instances of',
                str(unary_predicate),
                'See:', extended_theory_id)


def __check_if_relative_commitment_is_inferrable(
        wouldbe_committed_predicate: Predicate,
        wouldbe_committing_predicate: Predicate,
        subsumptions: list) -> bool:
    for relative_commitment in RelativeCommitments.registry:
        committed_predicate = relative_commitment.committed_predicate
        committing_predicate = relative_commitment.committing_predicate
        if wouldbe_committing_predicate == committing_predicate and [committed_predicate, wouldbe_committed_predicate] in subsumptions:
            return True
        if wouldbe_committed_predicate == committed_predicate and [wouldbe_committing_predicate, committing_predicate] in subsumptions:
            return True
        if [committed_predicate, wouldbe_committed_predicate] in subsumptions and [wouldbe_committing_predicate, committing_predicate] in subsumptions:
            return True
    return False
    