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
    run_time = 0
    vampire_modes = default_vampire_modes.copy()
    while len(vampire_modes) > 0:
        vampire_mode = vampire_modes[0]
        logging.info(msg=f'Using {vampire_mode} with time limit {time_limit}')
        vampire_path = os.path.join(project_root, 'resources/vampire')
        if vampire_mode == 'casc_sat':
            model_size = '-fmbss 35'
        else:
            model_size = str()
        cmd_to_run_vampire = \
            f'{vampire_path} --mode {vampire_mode} {model_size} -t {str(time_limit)} --cores 24 "{vampire_input_file_path}" > "{vampire_output_file_path}"'
        time_regex = re.compile(pattern=r'in time\s+(\d+\.\d+)\s+s')
        vampire_process = subprocess.Popen(cmd_to_run_vampire, shell=True)
        try:
            vampire_process.wait(timeout=time_limit + 1)
            # vampire_has_decided = vampire_process.returncode == 1
        except subprocess.TimeoutExpired as exception:
            logging.error(msg=str(exception))
            vampire_has_decided = True
        vampire_process.kill()
        # if vampire_has_decided:
        with open(vampire_output_file_path) as vampire_output_file:
            vampire_result = vampire_output_file.read()
        times = time_regex.findall(string=vampire_result)
        if len(times) == 1:
            single_run_time = float(times[0])
            run_time += single_run_time
        if 'SZS status Theorem' in vampire_result:
            return ProverResult.THEOREM, run_time
        elif 'SZS status Unsatisfiable' in vampire_result:
            return ProverResult.INCONSISTENT, run_time
        elif 'SZS status Satisfiable' in vampire_result:
            return ProverResult.CONSISTENT, run_time
        elif 'SZS status CounterSatisfiable' in vampire_result:
            return ProverResult.COUNTERSATISFIABLE, run_time
        elif 'SZS status Timeout' in vampire_result:
            if try_other_reasoner_modes:
                vampire_modes = vampire_modes[1:]
            else:
                return ProverResult.UNDECIDED, run_time
        else:
            logging.error(msg='Vampire hit a bump' + str(vampire_process))
            sys.exit(-1)

    return ProverResult.UNDECIDED, run_time
