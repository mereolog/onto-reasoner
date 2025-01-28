import logging
import random
import re

import pandas
from tqdm import tqdm

from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent
from wip.theory_processors.helpers import get_theory_id


def create_ml_training_data_from_axioms(cl_theory_axioms: list, results_intended_dist: dict, ml_data_path: str):
    ml_data = dict()
    results_dist = dict()
    
    ml_schema_dict = dict()
    for axiom in cl_theory_axioms:
        axiom_ids = re.findall(pattern=r'\[(.+)\]', string=axiom.comment)
        axiom_id = axiom_ids[0]
        ml_schema_dict[axiom] = axiom_id
    
    checked_theory_ids = set()
    try_again = True
    while try_again:
        random.shuffle(cl_theory_axioms)
        subtheory_size = random.randint(1,len(cl_theory_axioms))
        subtheory_axioms = cl_theory_axioms[:subtheory_size]
        subtheory_id = get_theory_id(subtheory_axioms)
        if subtheory_id in checked_theory_ids:
            continue
        checked_theory_ids.add(subtheory_id)
        subtheory = dict()
        subtheory['TheoryId'] = subtheory_id
        for axiom, axiom_id in ml_schema_dict.items():
            if axiom in subtheory_axioms:
                subtheory[axiom_id] = 1
            else:
                subtheory[axiom_id] = 0
        
        tptp_file_path = 'midputs/ml/tptp/' + subtheory_id + '.tptp'
        szs_file_path = 'midputs/ml/szs/' + subtheory_id + '.szs'
        cl_file_path = 'midputs/ml/cl/' + subtheory_id + '.cl'
        tptp_subtheory = str()
        cl_subtheory = str()
        for subtheory_axiom in subtheory_axioms:
            subtheory_axiom.is_self_standing = True
            tptp_subtheory += subtheory_axiom.to_tptp() + '\n'
            cl_subtheory += str(subtheory_axiom) + '\n'
        with open(file=tptp_file_path, mode='w') as tptp_theory_file:
            tptp_theory_file.write(tptp_subtheory)
        with open(file=cl_file_path, mode='w') as cl_theory_file:
            cl_theory_file.write(cl_subtheory)
            
        prover_result, time = (
            decide_whether_theory_is_consistent(
                vampire_input_file_path=tptp_file_path,
                vampire_output_file_path=szs_file_path,
                time=60 + len(subtheory_axioms)))
        logging.info(msg=subtheory_id + ' is ' + str(prover_result) + '. Checking this took ' + str(time) + ' seconds.')
        
        subtheory['ProverResult'] = str(prover_result)
        subtheory['AxiomCount'] = len(subtheory_axioms)
        ml_data[len(ml_data)] = subtheory
        bfo_report_dataframe = pandas.DataFrame.from_dict(data=ml_data, orient='index')
        bfo_report_dataframe.to_excel(ml_data_path, index=False)
        if prover_result in results_dist:
            results_dist[prover_result] += 1
        else:
            results_dist[prover_result] = 1
        try_again = False
        for prover_result, count in results_intended_dist.items():
            if prover_result not in results_dist or results_dist[prover_result] < count:
                try_again = True
                break


def create_ml_test_data_from_axioms(
        theory: list,
        theory_max_size: int,
        theory_min_size:int,
        dataset_length: int,
        ml_data_path: str,
        save_theories=False):
    ml_data = dict()
    ml_schema_dict = dict()
    for axiom in theory:
        axiom_ids = re.findall(pattern=r'\[(.+)\]', string=axiom.comment)
        axiom_id = axiom_ids[0]
        ml_schema_dict[axiom] = axiom_id
    
    checked_theory_ids = set()
    for index in tqdm(range(dataset_length)):
        random.shuffle(theory)
        subtheory_size = random.randint(theory_min_size, theory_max_size)
        subtheory_axioms = theory[:subtheory_size]
        subtheory_id = get_theory_id(subtheory_axioms)
        if subtheory_id in checked_theory_ids:
            continue
        checked_theory_ids.add(subtheory_id)
        subtheory = dict()
        subtheory['TheoryId'] = subtheory_id
        for axiom, axiom_id in ml_schema_dict.items():
            if axiom in subtheory_axioms:
                subtheory[axiom_id] = 1
            else:
                subtheory[axiom_id] = 0
        
        subtheory['ProverResult'] = None
        subtheory['AxiomCount'] = len(subtheory_axioms)
        ml_data[len(ml_data)] = subtheory
        if save_theories:
            tptp_file_path = './outputs/ml/tptp/' + subtheory_id + '.tptp'
            cl_file_path = './outputs/ml/cl/' + subtheory_id + '.cl'
            tptp_subtheory = str()
            cl_subtheory = str()
            for subtheory_axiom in subtheory_axioms:
                subtheory_axiom.is_self_standing = True
                tptp_subtheory += subtheory_axiom.to_tptp() + '\n'
                cl_subtheory += str(subtheory_axiom) + '\n'
            with open(file=tptp_file_path, mode='w') as tptp_theory_file:
                tptp_theory_file.write(tptp_subtheory)
            with open(file=cl_file_path, mode='w') as cl_theory_file:
                cl_theory_file.write(cl_subtheory)
        
    bfo_report_dataframe = pandas.DataFrame.from_dict(data=ml_data, orient='index')
    bfo_report_dataframe.to_excel(ml_data_path, index=False)

