import logging

from processors.reasoners.consistency_result import ProverResult
from wip.theory_processors.check_helper import check_theory
from wip.theory_processors.helpers import get_theory_id


def check_direct_subtheories_depthwise(
        theory: list,
        theory_axioms_to_ids: dict,
        checked_theory_ids: set,
        report_dict: dict,
        report_file_path: str = None,
        time_limit=180):
    consistent_count = 0
    undecided_count = 0
    theory_id = get_theory_id(theory)
    logging.info(msg='Checking all subtheories of theory ' + theory_id + ' of size: ' + str(len(theory)))
    for axiom in theory:
        subtheory_axioms = theory.copy()
        subtheory_axioms.remove(axiom)
        subtheory_id = get_theory_id(subtheory_axioms)
        
        if subtheory_id in checked_theory_ids:
            continue
        
        checked_theory_ids.add(subtheory_id)
        tptp_file_path = 'midputs/subtheories/tptp/' + subtheory_id + '.tptp'
        szs_file_path = 'midputs/subtheories/szs/' + subtheory_id + '.szs'
        cl_file_path = 'midputs/subtheories/cl/' + subtheory_id + '.cl'
        tptp_subtheory = str()
        cl_subtheory_axioms = list()
        cl_subtheory = str()
        
        for subtheory_axiom in subtheory_axioms:
            subtheory_axiom.is_self_standing = True
            tptp_subtheory += subtheory_axiom.to_tptp() + '\n'
            cl_subtheory_axioms.append(subtheory_axiom)
            cl_subtheory += str(subtheory_axiom.to_cl()) + '\n'
            
        with open(file=tptp_file_path, mode='w') as tptp_theory_file:
            tptp_theory_file.write(tptp_subtheory)
        with open(file=cl_file_path, mode='w') as cl_theory_file:
            cl_theory_file.write(cl_subtheory)

        check_result = (
            __check_subtheory(
                subtheory_axioms=subtheory_axioms,
                subtheory_id=subtheory_id,
                tptp_subtheory_string=tptp_subtheory,
                tptp_file_path=tptp_file_path,
                szs_file_path=szs_file_path,
                time_limit=time_limit,
                checked_theory_ids=checked_theory_ids,
                cl_theory_axioms_to_ids=theory_axioms_to_ids,
                report_dict=report_dict,
                report_file_path=report_file_path))
        if check_result == ProverResult.CONSISTENT:
            consistent_count += 1
        if check_result == ProverResult.UNDECIDED:
            undecided_count += 1
    
    logging.info(msg='All subtheories of theory ' + theory_id + ' have been checked.')
    logging.info(msg='There are ' + str(consistent_count) + ' consistent subtheories.')
    logging.info(msg='There are ' + str(undecided_count) + ' undecided subtheories.')


def __check_subtheory(
        subtheory_axioms: list,
        subtheory_id: str,
        tptp_subtheory_string: str,
        tptp_file_path: str,
        szs_file_path: str,
        time_limit: int,
        checked_theory_ids: set,
        cl_theory_axioms_to_ids: dict,
        report_dict: dict,
        report_file_path: str):

    check_result, time = (
        check_theory(
            theory=subtheory_axioms,
            theory_id=subtheory_id,
            tptp_file_path=tptp_file_path,
            szs_file_path=szs_file_path,
            time_limit=time_limit,
            theory_axioms_to_ids=cl_theory_axioms_to_ids,
            report_dict=report_dict,
            report_file_path=report_file_path,
            tptp_theory_string=tptp_subtheory_string))

    # if check_result == ProverResult.UNDECIDED:
    #     check_direct_subtheories_depthwise(
    #         theory=subtheory_axioms,
    #         theory_axioms_to_ids=cl_theory_axioms_to_ids,
    #         checked_theory_ids=checked_theory_ids,
    #         report_dict=report_dict,
    #         report_file_path=report_file_path)

