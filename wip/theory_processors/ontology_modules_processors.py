import logging
import os.path
import sys
from glob import glob
from itertools import chain, combinations
from os import path
from pathlib import Path

import pandas

from processors.reasoners.consistency_result import ProverResult
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from processors.utils.root_finder import find_project_root

MODULE_IDS_SEPARATOR = '+'

def find_n_undecided_supermodules(
        cl_theory_folder: str,
        prepare_cl_theory,
        parse_cl_theory,
        cl_supermodule_folder: str,
        n: int,
        report_dict: dict,
        report_file: str = None):
    logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.WARN, datefmt='%m/%d/%Y %I:%M:%S %p')
    
    project_root = find_project_root()
    
    undecided_supermodule_ids = set()
    theory_files = set()
    
    cl_theory_folder_path = os.path.join(project_root, cl_theory_folder)
    for filename in glob(pathname=cl_theory_folder_path, recursive=True):
        theory_files.add(filename)
    theory_files = list(theory_files)
    theory_files_subsets = chain.from_iterable(combinations(theory_files, r) for r in range(len(theory_files) + 1))
    for theory_files_subset in theory_files_subsets:
        supermodule = str()
        supermodule_id = str()
        for theory_file_path in theory_files_subset:
            with open(theory_file_path) as subtheory_file:
                supermodule += subtheory_file.read()
                supermodule_id += theory_file_path.split('/')[-1].replace('.cl','') + MODULE_IDS_SEPARATOR
        if len(theory_files_subset) > 0:
            supermodule_id = supermodule_id[:-1]
            ignore_supermodule = False
            for undecided_supermodule_id in undecided_supermodule_ids:
                supermodule_ids_set = set(supermodule_id.split(MODULE_IDS_SEPARATOR))
                undecided_supermodule_set = set(undecided_supermodule_id.split(MODULE_IDS_SEPARATOR))
                if undecided_supermodule_set.issubset(supermodule_ids_set):
                    ignore_supermodule = True
                    logging.warning(msg='Ignoring ' + supermodule_id + ' because of ' + undecided_supermodule_id)
                    break
            if ignore_supermodule:
                continue
            prepared_supermodule = prepare_cl_theory(bfo_clif=supermodule)
            supermodule_axioms = parse_cl_theory(text=prepared_supermodule)
            
            tptp_file_relative_path = 'resources/midputs/supermodules/tptp/' + supermodule_id + '.tptp'
            tptp_file_path = os.path.join(project_root, tptp_file_relative_path)
            szs_file__relative_path = 'resources/midputs/supermodules/szs/' + supermodule_id + '.szs'
            szs_file_path = os.path.join(project_root, szs_file__relative_path)
            
            with open(file=tptp_file_path, mode='w') as tptp_file, open(file=path.join(cl_supermodule_folder, supermodule_id), mode='w') as cl_file:
                for axiom in supermodule_axioms:
                    axiom.is_self_standing = True
                    tptp_file.write(axiom.to_tptp())
                    tptp_file.write('\n')
                    cl_file.write(str(axiom))
                    cl_file.write('\n')
            prover_result, time = (
                decide_whether_theory_is_consistent(
                    vampire_input_file_path=tptp_file_path,
                    vampire_output_file_path=szs_file_path,
                    time_limit=300 + len(supermodule_axioms)))
            report_dict[len(report_dict)] = \
                {
                    'theory_id': supermodule_id,
                    'theory_size': str(len(supermodule_axioms)),
                    'theory_status': str(prover_result),
                    'time_limit_offset': time
                }
            if report_file:
                report_file_path = os.path.join(project_root, report_file)
                bfo_report_dataframe = pandas.DataFrame.from_dict(data=report_dict, orient='index')
                bfo_report_dataframe.to_excel(report_file_path, index=False)
            if prover_result == ProverResult.CONSISTENT:
                logging.info(msg='Theory ' + supermodule_id + ' of size ' + str(len(supermodule_axioms)) + ' is consistent - it took ' + str(time) + ' to find it out.')
            if prover_result == ProverResult.UNDECIDED:
                logging.info(msg='Theory ' + supermodule_id + ' of size ' + str(len(supermodule_axioms)) + ' is undecided.')
                undecided_supermodule_ids.add(supermodule_id)
                if len(undecided_supermodule_ids) == n:
                    return
            if prover_result == ProverResult.INCONSISTENT:
                logging.warning(msg='Theory ' + supermodule_id + ' is inconsistent.')
                sys.exit(-1)
