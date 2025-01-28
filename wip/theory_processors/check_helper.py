import logging
import sys

import pandas

from processors.reasoners.consistency_result import ProverResult
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent


def check_theory(theory: list,
                 theory_id: str,
                 tptp_file_path: str,
                 szs_file_path: str,
                 time_limit: int,
                 theory_axioms_to_ids: dict,
                 report_dict: dict,
                 report_file_path: str,
                 tptp_theory_string: str,
                 try_other_reasoner_modes = False) -> tuple:
    logging.info(msg='Checking theory ' + theory_id + ' of size: ' + str(len(theory)))

    check_result, time = (
        decide_whether_theory_is_consistent(
            vampire_input_file_path=tptp_file_path,
            vampire_output_file_path=szs_file_path,
            time=time_limit + len(theory),
            try_other_reasoner_modes=try_other_reasoner_modes))

    new_time_limit = time_limit * 4
    if check_result == ProverResult.UNDECIDED:
        if new_time_limit <= 360:
            logging.info(msg='Rechecking ' + theory_id + ' with time offset of ' + str(new_time_limit) + ' seconds.')
            check_result, time = (
                check_theory(
                    theory=theory,
                    theory_id=theory_id,
                    tptp_file_path=tptp_file_path,
                    szs_file_path=szs_file_path,
                    time_limit=new_time_limit,
                    theory_axioms_to_ids=theory_axioms_to_ids,
                    report_dict=report_dict,
                    report_file_path=report_file_path,
                    tptp_theory_string=tptp_theory_string,
                    try_other_reasoner_modes=True))

    report_result = \
        {
            'theory_id': theory_id,
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
        bfo_report_dataframe.to_excel(report_file_path, index=False)

    if check_result == ProverResult.CONSISTENT:
        logging.info(msg=theory_id + ' is consistent - checking this took ' + str(time) + ' seconds.')

    if check_result == ProverResult.UNDECIDED:
        logging.info(msg=theory_id + ' is undecided - checking this took ' + str(time) + ' seconds.')
        with open(file='outputs/undecided/' + theory_id + '.tptp', mode='w') as undecided_tptp_theory:
            undecided_tptp_theory.write(tptp_theory_string)

    if check_result == ProverResult.INCONSISTENT:
        logging.info(msg=theory_id + ' is inconsistent.')
        with open(file='outputs/decided/inconsistent/' + theory_id + '.tptp', mode='w') as inconsistent_tptp_theory:
            inconsistent_tptp_theory.write(tptp_theory_string)
        sys.exit(-1)

    return check_result, time
