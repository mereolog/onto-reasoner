import logging

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.clif_parser import parse_clif
from wip.theory_processors.extenders import extend_theory_with_domain_size

# from theory_processors.subtheories_checker import check_half_split_subtheories_depthwise

logging.basicConfig(format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO,datefmt='%m/%d/%Y %I:%M:%S %p')
with open('../resources/midputs/bfo.cl') as bfo_file:
    bfo_clif = bfo_file.read()
prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = list(parse_clif(text=prepared_bfo))
domain_restricted_bfo_theory = extend_theory_with_domain_size(theory=bfo_theory,domain_size=35)
with open('midputs/bfo_size_'+str(35)+'.tptp', mode='w') as bfo_domain_restriced_theory_file:
    for axiom in domain_restricted_bfo_theory:
        axiom.is_self_standing = True
        bfo_domain_restriced_theory_file.write(str(axiom.to_tptp()))
        bfo_domain_restriced_theory_file.write('\n')
