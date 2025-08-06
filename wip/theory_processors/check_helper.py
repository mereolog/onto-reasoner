import logging
import os.path
import sys

import pandas

from processors.reasoners.consistency_result import ProverResult
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from processors.utils.root_finder import find_project_root


def check_theory(
        theory: list,
         theory_id: str,
         tptp_file_path: str,
         szs_file_path: str,
         time_limit_offset: int,
         theory_axioms_to_ids: dict,
         report_dict: dict,
         report_file_path: str,
         tptp_theory_string: str,
         try_other_reasoner_modes = True,
         parent_theory_id=str()) -> tuple:
    logging.info(msg=f'Checking theory {theory_id} (subtheory of {parent_theory_id}) of size {str(len(theory))}')
    
    project_root = find_project_root()

    check_result, time = (
        decide_whether_theory_is_consistent(
            vampire_input_file_path=tptp_file_path,
            vampire_output_file_path=szs_file_path,
            time_limit=time_limit_offset + len(theory),
            try_other_reasoner_modes=try_other_reasoner_modes))

    report_result = \
        {
            'theory_id': theory_id,
            'parent_theory_id': parent_theory_id,
            'theory_size': str(len(theory)),
            'theory_status': str(check_result),
            'time': time
        }

    for cl_axiom, cl_axiom_id in theory_axioms_to_ids.items():
        if cl_axiom in theory:
            report_result[cl_axiom_id] = 1
        else:
            report_result[cl_axiom_id] = 0

    report_dict[len(report_dict)] = report_result

    if report_file_path:
        bfo_report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
        bfo_report_dataframe.to_excel(os.path.join(project_root, report_file_path), index=False)

    if check_result == ProverResult.CONSISTENT:
        logging.info(msg=theory_id + ' is consistent - checking this took ' + str(time) + ' seconds.')

    if check_result == ProverResult.UNDECIDED:
        logging.info(msg=theory_id + ' is undecided - checking this took ' + str(time) + ' seconds.')
        with open(file=os.path.join(project_root, 'resources/outputs/undecided/') + theory_id + '.tptp', mode='w') as undecided_tptp_theory:
            undecided_tptp_theory.write(tptp_theory_string)

    if check_result == ProverResult.INCONSISTENT:
        logging.info(msg=theory_id + ' is inconsistent.')
        with open(file=os.path.join(project_root, 'outputs/decided/inconsistent/') + theory_id + '.tptp', mode='w') as inconsistent_tptp_theory:
            inconsistent_tptp_theory.write(tptp_theory_string)
        sys.exit(-1)

    return check_result, time
