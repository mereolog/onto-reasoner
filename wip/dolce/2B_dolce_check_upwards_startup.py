import logging

from wip.theory_processors import check_direct_supertheories_depthwise

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')

import logging

from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from wip.theory_processors.helpers import create_cl_theory_signature

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
with open('midputs/instantiated_dolce.cl') as dolce_file:
    cl_dolce_text = dolce_file.read()
dolce_theory = extended_parse_clif(text=cl_dolce_text)
dolce_theory_signature = create_cl_theory_signature(cl_theory_axioms=dolce_theory)
base_theory = dolce_theory[:164]
check_direct_supertheories_depthwise(
    main_theory=dolce_theory,
    report_dict=dict(),
    report_file_path='outputs/dolce_check_upward_generation_report.xlsx',
    base_theory=base_theory,
    theory_axioms_to_ids=dolce_theory_signature,
    checked_theory_ids=set(),
    time_limit=60)
