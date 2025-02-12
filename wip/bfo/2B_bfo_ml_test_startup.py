import logging

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from wip.ml_preparers.ml_data_creator_from_scratch import create_ml_test_data_from_axioms

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
with open('midputs/bfo_small.cl') as bfo_file:
    bfo_clif = bfo_file.read()
prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = list(extended_parse_clif(text=prepared_bfo))
bfo_theory.sort()
create_ml_test_data_from_axioms(
    theory=bfo_theory,
    ml_data_path='/Users/pawel.garbacz/Desktop/bfo_ml_test_data.xlsx',
    dataset_length=10000,
    theory_max_size=128,
    theory_min_size=32)