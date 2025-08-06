import logging
import os.path

from processors.reasoners.consistency_result import ProverResult
from processors.utils.root_finder import find_project_root
from wip.theory_processors.check_helper import check_theory
from wip.theory_processors.helpers import get_theory_id


def check_direct_subtheories_depthwise(
        theory: list,
        theory_axioms_to_ids: dict,
        checked_theory_ids: set,
        report_dict: dict,
        report_file_path: str = None,
        time_limit_offset=180) -> bool:
    project_root = find_project_root()
    
    tptp_theory = str()
    for theory_axiom in theory:
        theory_axiom.is_self_standing = True
        tptp_theory += theory_axiom.to_tptp() + '\n'
    
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
        tptp_file_path = os.path.join(project_root,'resources/midputs/subtheories/tptp/') + subtheory_id + '.tptp'
        szs_file_path = os.path.join(project_root, 'resources/midputs/subtheories/szs/') + subtheory_id + '.szs'
        cl_file_path = os.path.join(project_root,'resources/midputs/subtheories/cl/') + subtheory_id + '.cl'
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
        
        consistent_count, undecided_count = (
            __check_subtheory(
                subtheory_axioms=subtheory_axioms,
                subtheory_id=subtheory_id,
                tptp_subtheory_string=tptp_subtheory,
                tptp_file_path=tptp_file_path,
                szs_file_path=szs_file_path,
                time_limit_offset=time_limit_offset,
                checked_theory_ids=checked_theory_ids,
                cl_theory_axioms_to_ids=theory_axioms_to_ids,
                report_dict=report_dict,
                report_file_path=report_file_path,
                parent_theory_id=theory_id,
                consistent_count=consistent_count,
                undecided_count=undecided_count))
    
    logging.info(msg='All subtheories of theory ' + theory_id + ' have been checked.')
    logging.info(msg='There are ' + str(consistent_count) + ' consistent subtheories.')
    logging.info(msg='There are ' + str(undecided_count) + ' undecided subtheories.')
    if consistent_count == len(theory):
        new_time_limit_offset = time_limit_offset
        check_result = ProverResult.UNDECIDED
        while new_time_limit_offset <= time_limit_offset * 6:
            new_time_limit_offset = new_time_limit_offset * 2
            logging.info(msg=f'Rechecking {theory_id} with time_limit_offset of {str(new_time_limit_offset)} seconds.')
            
            tptp_file_path = os.path.join(project_root, 'resources/midputs/subtheories/tptp/') + theory_id + '.tptp'
            szs_file_path = os.path.join(project_root, 'resources/midputs/subtheories/szs/') + theory_id + '.szs'
            check_result, time = (
                check_theory(
                    theory_id=theory_id,
                    tptp_file_path=tptp_file_path,
                    szs_file_path=szs_file_path,
                    tptp_theory_string=tptp_theory,
                    theory=theory,
                    theory_axioms_to_ids=theory_axioms_to_ids,
                    report_dict=report_dict,
                    report_file_path=report_file_path,
                    time_limit_offset=new_time_limit_offset,
                    parent_theory_id=theory_id))
            if check_result == ProverResult.CONSISTENT:
                return True
        if check_result == ProverResult.UNDECIDED:
            print(f'Theory {theory_id} is a tough nut case.')
    return False


def __check_subtheory(
        subtheory_axioms: list,
        subtheory_id: str,
        tptp_subtheory_string: str,
        tptp_file_path: str,
        szs_file_path: str,
        time_limit_offset: int,
        checked_theory_ids: set,
        cl_theory_axioms_to_ids: dict,
        report_dict: dict,
        report_file_path: str,
        parent_theory_id: str,
        consistent_count: int,
        undecided_count:int) -> tuple:

    check_result, time = (
        check_theory(
            theory=subtheory_axioms,
            theory_id=subtheory_id,
            tptp_file_path=tptp_file_path,
            szs_file_path=szs_file_path,
            time_limit_offset=time_limit_offset,
            theory_axioms_to_ids=cl_theory_axioms_to_ids,
            report_dict=report_dict,
            report_file_path=report_file_path,
            tptp_theory_string=tptp_subtheory_string,
            parent_theory_id=parent_theory_id))
    
    if check_result == ProverResult.CONSISTENT:
        consistent_count += 1

    if check_result == ProverResult.UNDECIDED:
        undecided_count += 1
        is_theory_consistent = (
            check_direct_subtheories_depthwise(
                theory=subtheory_axioms,
                theory_axioms_to_ids=cl_theory_axioms_to_ids,
                checked_theory_ids=checked_theory_ids,
                report_dict=report_dict,
                report_file_path=report_file_path,
                time_limit_offset=time_limit_offset))
    
    if is_theory_consistent:
        undecided_count -= 1
        consistent_count += 1
    return consistent_count, undecided_count
