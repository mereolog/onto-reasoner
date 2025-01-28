from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.parsers.extended_clif_parser import extended_parse_clif
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from wip.theory_processors.helpers import get_theory_id

# clone_repo(repo_github_url='https://github.com/BFO-ontology/BFO-2020.git', clone_folder='bfo')

# concatenate_files_in_folder(
#     input_folder_path='inputs/bfo/src/common-logic',
#     input_files_extension='cl',
#     output_file_path='midputs/bfo.cl')

with open('midputs/bfo.cl') as bfo_file:
    bfo_clif = bfo_file.read()
prepared_bfo = prepare_clif_bfo(bfo_clif=bfo_clif)
bfo_theory = extended_parse_clif(text=prepared_bfo)
bfo_theory.sort()
stronger_axioms = set()
with open('midputs/test.tptp', mode='w') as bfo_tptp:
    for axiom in bfo_theory:
        stronger_axiom = axiom.make_stronger(inverse_strength=False)
        stronger_axiom.is_self_standing = True
        stronger_axioms.add(stronger_axiom)
stronger_bfo_theories = set()
for stronger_axiom in stronger_axioms:
    stronger_bfo_theory = bfo_theory.copy()
    stronger_bfo_theory.append(stronger_axiom)
    stronger_bfo_theory_id = get_theory_id(stronger_bfo_theory)
    with open('midputs/stronger/'+stronger_bfo_theory_id+'.tptp', mode='w') as bfo_tptp_file:
        for axiom in stronger_bfo_theory:
            bfo_tptp_file.write(axiom.to_tptp())
            bfo_tptp_file.write('\n')
            bfo_tptp_file.flush()
    check_result, time = (
        decide_whether_theory_is_consistent(
            vampire_input_file_path='midputs/stronger/'+stronger_bfo_theory_id+'.tptp',
            vampire_output_file_path='midputs/stronger/'+stronger_bfo_theory_id+'.szs',
            time=360))
    print(stronger_bfo_theory_id, 'is found', check_result, 'after', str(time), 'seconds.')


