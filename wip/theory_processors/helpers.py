import re
import uuid

from objects.fol_logic.objects.formula import Formula


def get_theory_id(theory: list) -> str:
    theory_copy = theory.copy()
    theory_copy.sort()
    return uuid.uuid5(uuid.NAMESPACE_OID, str(theory_copy)).hex

def get_axiom_id(axiom: Formula) -> str:
    return uuid.uuid5(uuid.NAMESPACE_OID, str(axiom)).hex

def create_cl_theory_signature(cl_theory_axioms: list) -> dict:
    cl_theory_signature = dict()
    for axiom in cl_theory_axioms:
        if axiom.comment:
            axiom_ids = re.findall(pattern=r'\[(.+)\]', string=axiom.comment)
            axiom_id = axiom_ids[0]
        else:
            axiom_id = get_axiom_id(axiom)
        cl_theory_signature[axiom] = axiom_id
    return cl_theory_signature