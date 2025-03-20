import logging
import sys

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.clif_parser import parse_clif
from wip.theory_processors.ontology_modules_processors import find_n_undecided_supermodules

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
find_n_undecided_supermodules(
    cl_theory_path='./inputs/bfo/src/common-logic/**/*.cl',
    cl_module_path='midputs/supermodules/cl/',
    prepare_cl_theory=prepare_clif_bfo,
    parse_cl_theory=parse_clif,
    n=sys.maxsize,
    report_dict=dict(),
    report_file_path='./midputs/supermodules/bfo_supermodules_generation_report.xlsx')