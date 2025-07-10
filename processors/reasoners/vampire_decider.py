import logging
import os.path
import re
import subprocess
import sys

from processors.reasoners.consistency_result import ProverResult
from processors.utils.root_finder import find_project_root

default_vampire_modes = ['casc_sat', 'casc', 'portfolio']


def decide_whether_theory_is_consistent(
        vampire_input_file_path: str,
        vampire_output_file_path: str,
        time_limit: int=300,
        try_other_reasoner_modes=False) -> tuple:
    project_root = find_project_root()
    
    vampire_modes = default_vampire_modes.copy()
    while len(vampire_modes) > 0:
        time=-1
        vampire_mode = vampire_modes[0]
        logging.info(msg=f'Using {vampire_mode} with time limit {time_limit}')
        vampire_path = os.path.join(project_root, 'resources/vampire')
        cmd_to_run_vampire = vampire_path + ' --mode ' + vampire_mode + ' -t ' + str(time_limit) + ' --cores 24 "' + vampire_input_file_path + '" > "' + vampire_output_file_path + '"'
        time_regex = re.compile(pattern=r'in time\s+(\d+\.\d+)\s+s')
        vampire_process = subprocess.Popen(cmd_to_run_vampire, shell=True)
        try:
            vampire_process.wait(timeout=time_limit + 1)
            vampire_has_decided = vampire_process.returncode == 1
        except subprocess.TimeoutExpired as exception:
            logging.error(msg=str(exception))
            vampire_has_decided = True
        vampire_process.kill()
        if vampire_has_decided:
            with open(vampire_output_file_path) as vampire_output_file:
                vampire_result = vampire_output_file.read()
            times = time_regex.findall(string=vampire_result)
            if len(times) == 1:
                time = float(times[0])
            if 'SZS status Theorem' in vampire_result:
                return ProverResult.THEOREM, time
            elif 'SZS status Unsatisfiable' in vampire_result:
                return ProverResult.INCONSISTENT, time
            elif 'SZS status Satisfiable' in vampire_result:
                return ProverResult.CONSISTENT, time
            elif 'SZS status CounterSatisfiable' in vampire_result:
                return ProverResult.COUNTERSATISFIABLE, time
            elif 'SZS status Timeout' in vampire_result:
                if try_other_reasoner_modes:
                    vampire_modes = vampire_modes[1:]
                else:
                    return ProverResult.UNDECIDED, time
            else:
                logging.error(msg='Vampire hit a bump' + str(vampire_process))
                sys.exit(-1)
        if try_other_reasoner_modes:
            vampire_modes = vampire_modes[1:]
        else:
            return ProverResult.UNDECIDED, time
    return ProverResult.UNDECIDED, time
