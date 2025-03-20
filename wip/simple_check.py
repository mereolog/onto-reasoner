from processors.reasoners.vampire_decider import decide_whether_theory_is_consistent

decide_whether_theory_is_consistent(
    vampire_input_file_path='../resources/midputs/bfo_min_undecided.tptp',
    vampire_output_file_path='../resources/midputs/bfo_min_undecided.szs')