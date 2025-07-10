from processors.readers.parsers.clif_parser import parse_clif


def translate_cl_2_tptp_theory(cl_file: str, tptp_file: str):
    with open(cl_file) as cl_file:
        cl_text = cl_file.read()
    cl_theory = parse_clif(cl_text)
    with open(tptp_file, mode='w') as tptp_file:
        for axiom in cl_theory:
            axiom.is_self_standing = True
            tptp_file.write(axiom.to_tptp())
            tptp_file.write('\n')
