from processors.readers.parsers.extended_clif_parser import extended_parse_clif

# clone_repo(repo_github_url='https://github.com/BFO-ontology/BFO-2020.git', clone_folder='bfo')

# concatenate_files_in_folder(
#     input_folder_path='inputs/bfo/src/common-logic',
#     input_files_extension='cl',
#     output_file_path='midputs/bfo.cl')

with open('midputs/instantiated_dolce.cl') as bfo_file:
    instantiated_dolce_text = bfo_file.read()
dolce_theory = extended_parse_clif(instantiated_dolce_text)
dolce_theory.sort()
with open('midputs/instantiated_dolce.tptp', mode='w') as dolce_tptp_file:
    for axiom in dolce_theory:
        axiom.is_self_standing = True
        dolce_tptp_file.write(axiom.to_tptp())
        dolce_tptp_file.write('\n')

