from processors.reasoners.consistency_result import ProverResult
from wip.theory_processors.check_helper import check_theory
from wip.theory_processors.helpers import get_theory_id
from wip.theory_processors.neighbours_crawler import find_neighbouring_supertheory
from wip.theory_processors.supertheories_checker import check_direct_supertheories_depthwise


def check_neighbours(
        main_theory: list,
        base_theory: list,
        theory_axioms_to_ids: dict,
        report_dict: dict,
        report_file_path: str = None,
        time_limit=180):
    checked_theory_ids = set()
    neighbouring_supertheory = find_neighbouring_supertheory(main_theory=main_theory, theory=base_theory)
    neighbouring_supertheory_id = get_theory_id(neighbouring_supertheory)

    tptp_file_path = 'midputs/neighbours/tptp/' + neighbouring_supertheory_id + '.tptp'
    szs_file_path = 'midputs/neighbours/szs/' + neighbouring_supertheory_id + '.szs'
    cl_file_path = 'midputs/neighbours/cl/' + neighbouring_supertheory_id + '.cl'
    tptp_subtheory_string = str()
    cl_subtheory_axioms = list()
    cl_subtheory_string = str()

    for subtheory_axiom in neighbouring_supertheory:
        subtheory_axiom.is_self_standing = True
        tptp_subtheory_string += subtheory_axiom.to_tptp() + '\n'
        cl_subtheory_axioms.append(subtheory_axiom)
        cl_subtheory_string += str(subtheory_axiom.to_cl()) + '\n'

    with open(file=tptp_file_path, mode='w') as tptp_theory_file:
        tptp_theory_file.write(tptp_subtheory_string)
    with open(file=cl_file_path, mode='w') as cl_theory_file:
        cl_theory_file.write(cl_subtheory_string)

    check_result, time = (
        check_theory(
            theory=neighbouring_supertheory,
            theory_id=neighbouring_supertheory_id,
            tptp_file_path=tptp_file_path,
            szs_file_path=szs_file_path,
            report_dict=report_dict,
            report_file_path=report_file_path,
            time_limit=time_limit,
            theory_axioms_to_ids=theory_axioms_to_ids,
            tptp_theory_string=tptp_subtheory_string))

    checked_theory_ids.add(neighbouring_supertheory_id)

    if check_result == ProverResult.CONSISTENT:
        check_direct_supertheories_depthwise(
            main_theory=main_theory,
            report_dict=report_dict,
            report_file_path=report_file_path,
            base_theory=neighbouring_supertheory,
            theory_axioms_to_ids=theory_axioms_to_ids,
            checked_theory_ids=set(),
            time_limit=180)