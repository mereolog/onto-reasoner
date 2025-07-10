import os.path
from glob import glob

from processors.preparers.bfo_preparer import prepare_clif_bfo
from processors.readers.files_concatenator import concatenate_cl_files_in_folder
from processors.translator.cl_2_tptp_translator import translate_cl_2_tptp_theory
from processors.utils.root_finder import find_project_root

project_root = find_project_root()

concatenate_cl_files_in_folder(
    root_folder='resources/midputs/bfo_undecided/',
    output_file='resources/midputs/bfo_undecided.cl')

bfo_file_path = os.path.join(project_root, 'resources/midputs/bfo_undecided.cl')
with open(bfo_file_path) as bfo_file:
    bfo_clif = bfo_file.read()
bfo_clif = prepare_clif_bfo(bfo_clif)
prepared_bfo_file_path = os.path.join(project_root, 'resources/midputs/prepared_bfo_undecided.cl')
with open(prepared_bfo_file_path, mode='w') as bfo_file:
    bfo_file.write(bfo_clif)

translate_cl_2_tptp_theory(
    tptp_file=os.path.join(project_root,'resources/midputs/prepared_bfo_undecided.tptp'),
    cl_file=os.path.join(project_root,'resources/midputs/prepared_bfo_undecided.cl'))

