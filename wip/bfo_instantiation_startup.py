from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from wip.theory_processors import instantiate_cl_theory

with open('../resources/midputs/bfo_min_undecided.cl') as bfo_file:
    bfo_clif = bfo_file.read()
# prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = extended_parse_clif(text=bfo_clif)

instantiate_cl_theory(
    cl_theory=bfo_theory,
    cl_theory_file_path=str(),
    instantiated_cl_theory_file_path='../resources/midputs/instantiated_bfo_min_undecided.cl')