from processors.readers.parsers.tptp_parser import parse_tptp
from processors.reasoners.consistency_result import ProverResult
from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from wip.theory_processors.helpers import get_theory_id

with open('../resources/midputs/instantiated_dolce.tptp') as dolce_file:
    dolce_tptp_text = dolce_file.read()
dolce_theory = parse_tptp(dolce_tptp_text)
dolce_theory.sort()
stronger_axioms = set()
predicates = set()
for axiom in dolce_theory:
    stronger_axiom = axiom.make_stronger(inverse_strength=False)
    axiom_predicates = axiom.get_all_predicates()
    predicates = predicates.union(axiom_predicates)
    if str(stronger_axiom) == str(axiom):
        continue
    stronger_axiom.is_self_standing = True
    stronger_axioms.add(stronger_axiom)

stronger_dolce_theories = set()
for stronger_axiom in stronger_axioms:
    stronger_dolce_theory = dolce_theory.copy()
    stronger_dolce_theory.append(stronger_axiom)
    stronger_dolce_theory_id = get_theory_id(stronger_dolce_theory)
    with open('midputs/stronger/dolce/'+stronger_dolce_theory_id+'.tptp', mode='w') as stronger_dolce_tptp_file:
        for axiom in stronger_dolce_theory:
            stronger_dolce_tptp_file.write(axiom.to_tptp())
            stronger_dolce_tptp_file.write('\n')
            stronger_dolce_tptp_file.flush()
    check_result, time = (
        decide_whether_theory_is_consistent(
            vampire_input_file_path='midputs/stronger/dolce/'+stronger_dolce_theory_id+'.tptp',
            vampire_output_file_path='midputs/stronger/dolce/'+stronger_dolce_theory_id+'.szs',
            time=60))
    if not check_result == ProverResult.INCONSISTENT:
        print('Theory', stronger_dolce_theory_id, 'with axiom', str(stronger_axiom), 'is found', check_result, 'after', str(time), 'seconds.')


