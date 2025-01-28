import logging

from wip.ml_preparers.ml_data_creator_from_scratch import create_ml_training_data_from_axioms
from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from processors.reasoners import ProverResult

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
with open('midputs/subtheories/cl/-2902263708894172198.cl') as bfo_file:
    bfo_clif = bfo_file.read()
prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = list(extended_parse_clif(text=bfo_clif))
bfo_theory.sort()
results_intended_dist = {ProverResult.CONSISTENT: 100, ProverResult.UNDECIDED: 10}
create_ml_training_data_from_axioms(
    cl_theory_axioms=bfo_theory,
    ml_data_path='./outputs/bfo_ml_train_data.xlsx',
    results_intended_dist=results_intended_dist)