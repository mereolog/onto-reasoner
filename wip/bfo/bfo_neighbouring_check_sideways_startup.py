import logging

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.clif_parser import parse_clif
from wip.theory_processors.helpers import create_cl_theory_signature
from wip.theory_processors.neighbours_checker import check_neighbours

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')

with open('midputs/bfo_small.cl') as bfo_file:
    bfo_clif = bfo_file.read()
prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = parse_clif(text=prepared_bfo)
base_theory = list()
for bfo_axiom in bfo_theory:
    if '[mbf-1]' in bfo_axiom.comment:
        base_theory.append(bfo_axiom)
bfo_cl_theory_signature = create_cl_theory_signature(cl_theory_axioms=bfo_theory)
bfo_theory.sort()
check_neighbours(
    main_theory=bfo_theory,
    base_theory=base_theory,
    theory_axioms_to_ids=bfo_cl_theory_signature,
    report_dict=dict(),
    report_file_path='',
    time_limit=180)

