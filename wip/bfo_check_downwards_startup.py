import logging

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from wip.theory_processors.helpers import create_cl_theory_signature
from wip.theory_processors.subtheories_checker import check_direct_subtheories_depthwise

# from theory_processors.subtheories_checker import check_half_split_subtheories_depthwise

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
with open('../resources/midputs/bfo_undecided_fragment.cl') as bfo_file:
    bfo_clif = bfo_file.read()
bfo_clif = prepare_clif_bfo(bfo_clif)
bfo_theory = list(extended_parse_clif(text=bfo_clif))
bfo_cl_theory_signature = create_cl_theory_signature(cl_theory_axioms=bfo_theory)
bfo_theory.sort()
bfo_report = (
    check_direct_subtheories_depthwise(
        theory=bfo_theory,
        theory_axioms_to_ids=bfo_cl_theory_signature,
        checked_theory_ids=set(),
        report_dict=dict(),
        report_file_path='../resources/outputs/bfo_submodules_downward_generation_report.xlsx',
        time_limit=300))

