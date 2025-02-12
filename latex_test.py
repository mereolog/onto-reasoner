from processors.readers.parsers.extended_clif_parser import extended_parse_clif

with open('resources/midputs/dolce.cl') as cl_theory_file:
    cl_theory_text = cl_theory_file.read()
cl_theory_axioms = extended_parse_clif(cl_theory_text)
for axiom in cl_theory_axioms:
    print(axiom.to_latex())