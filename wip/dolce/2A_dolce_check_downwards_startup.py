import logging

from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from wip.theory_processors.helpers import create_cl_theory_signature
from wip.theory_processors.subtheories_checker import check_direct_subtheories_depthwise

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
with open('midputs/instantiated_dolce.cl') as dolce_file:
    cl_dolce_text = dolce_file.read()
dolce_theory = extended_parse_clif(text=cl_dolce_text)
dolce_theory_signature = create_cl_theory_signature(cl_theory_axioms=dolce_theory)
dolce_theory.sort()
dolce_report = (
    check_direct_subtheories_depthwise(
        theory=dolce_theory,
        theory_axioms_to_ids=dolce_theory_signature,
        checked_theory_ids=set(),
        report_dict=dict(),
        report_file_path='outputs/dolce_subtheories_generation_report.xlsx'))

