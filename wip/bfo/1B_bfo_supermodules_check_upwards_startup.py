import logging

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.clif_parser import parse_clif
from wip.theory_processors.helpers import create_cl_theory_signature
from wip.theory_processors.supertheories_checker import check_direct_supertheories_depthwise

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')

with open('midputs/bfo_small.cl') as bfo_file:
    bfo_clif = bfo_file.read()
prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = parse_clif(text=prepared_bfo)
base_theory = list()
for bfo_axiom in bfo_theory:
    if '[mbf-1]' in bfo_axiom.comment:
        base_theory.append(bfo_axiom)
bfo_theory.sort()
bfo_cl_theory_signature = create_cl_theory_signature(cl_theory_axioms=bfo_theory)
check_direct_supertheories_depthwise(
    main_theory=bfo_theory,
    report_dict=dict(),
    report_file_path='outputs/bfo_submodules_upward_generation_report.xlsx',
    base_theory=base_theory,
    theory_axioms_to_ids=bfo_cl_theory_signature,
    checked_theory_ids=set(),
    time_limit=180)
