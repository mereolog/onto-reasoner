import logging
from itertools import combinations

from processors.reasoners.consistency_result import ProverResult
from wip.theory_processors.check_helper import check_theory
from wip.theory_processors.helpers import get_theory_id


def powerset_of_size(iterable, size: int) -> set:
    s = list(iterable)
    return combinations(s, size)


def check_direct_supertheories_depthwise(
        main_theory: list,
        base_theory: list,
        theory_axioms_to_ids: dict,
        checked_theory_ids: set,
        report_dict: dict,
        report_file_path: str = None,
        time_limit=180):
    theory_id = get_theory_id(base_theory)
    logging.info(msg='Checking all direct supertheories of theory ' + theory_id + ' of size: ' + str(len(base_theory)))
    for axiom in main_theory:
        if axiom in base_theory:
            continue
        supertheory_axioms = base_theory.copy()
        supertheory_axioms.append(axiom)
        supertheory_id = get_theory_id(supertheory_axioms)
        if supertheory_id in checked_theory_ids:
            continue
        if set(supertheory_axioms) == set(main_theory):
            continue
        tptp_file_path = 'midputs/supertheories/tptp/' + supertheory_id + '.tptp'
        szs_file_path = 'midputs/supertheories/szs/' + supertheory_id + '.szs'
        cl_file_path = 'midputs/supertheories/cl/' + supertheory_id + '.cl'

        tptp_supertheory_string = str()
        cl_supertheory_string = str()
        clif_supertheory = list()
        for supertheory_axiom in supertheory_axioms:
            supertheory_axiom.is_self_standing = True
            tptp_supertheory_string += supertheory_axiom.to_tptp() + '\n'
            clif_supertheory.append(supertheory_axiom)
            cl_supertheory_string += str(supertheory_axiom.to_cl()) + '\n'
        with open(file=tptp_file_path, mode='w') as tptp_theory_file:
            tptp_theory_file.write(tptp_supertheory_string)
        with open(file=cl_file_path, mode='w') as cl_theory_file:
            cl_theory_file.write(cl_supertheory_string)
        checked_theory_ids.add(supertheory_id)

        __check_supertheory(
            main_theory_axioms=main_theory,
            supertheory_axioms=supertheory_axioms,
            supertheory_id=supertheory_id,
            tptp_supertheory_string=tptp_supertheory_string,
            tptp_file_path=tptp_file_path,
            szs_file_path=szs_file_path,
            time_limit=time_limit,
            checked_theory_ids=checked_theory_ids,
            cl_theory_axioms_to_ids=theory_axioms_to_ids,
            report_dict=report_dict,
            report_file_path=report_file_path)


def __check_supertheory(
        main_theory_axioms: list,
        supertheory_axioms: list,
        supertheory_id: str,
        tptp_supertheory_string: str,
        tptp_file_path: str,
        szs_file_path: str,
        time_limit: int,
        checked_theory_ids: set,
        cl_theory_axioms_to_ids: dict,
        report_dict: dict,
        report_file_path: str):
    if set(main_theory_axioms) == set(supertheory_axioms):
        return

    check_result, time = (
        check_theory(
            theory=supertheory_axioms,
            theory_id=supertheory_id,
            tptp_file_path=tptp_file_path,
            szs_file_path=szs_file_path,
            time_limit=time_limit,
            theory_axioms_to_ids=cl_theory_axioms_to_ids,
            report_dict=report_dict,
            report_file_path=report_file_path,
            tptp_theory_string=tptp_supertheory_string))

    if check_result == ProverResult.CONSISTENT:
        check_direct_supertheories_depthwise(
            main_theory=main_theory_axioms,
            base_theory=supertheory_axioms,
            time_limit=time_limit,
            checked_theory_ids=checked_theory_ids,
            theory_axioms_to_ids=cl_theory_axioms_to_ids,
            report_dict=report_dict,
            report_file_path=report_file_path)

