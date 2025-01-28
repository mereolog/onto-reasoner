from processors.readers.parsers import parse_tptp


def translate_tptp_2_cl_theory(tptp_file_path: str, cl_file_path: str):
    with open(tptp_file_path) as tptp_file:
        tptp_text = tptp_file.read()
    tptp_theory = parse_tptp(tptp_text)
    with open(cl_file_path, mode='w') as cl_file:
        for axiom in tptp_theory:
            axiom.is_self_standing = True
            cl_file.write(axiom.to_cl())
            cl_file.write('\n')
