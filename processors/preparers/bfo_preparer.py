import re

def __fix_quote_marks(bfo: str) -> str:
    fixed_bfo = bfo.replace("'", "\\'")
    fixed_bfo = fixed_bfo.replace('"', "'")
    return fixed_bfo


def __extract_axioms(bfo: str) -> str:
    bfo_out_discource_pattern = re.compile(pattern=r'\(cl:outdiscourse.+')
    bfo = bfo_out_discource_pattern.sub(repl='', string=bfo)
    bfo_axiom_pattern = re.compile(pattern=r'\n\s+\(cl:comment\s+.+?\)\n\n', flags=re.DOTALL)
    bfo_axioms = bfo_axiom_pattern.findall(string=bfo)
    bfo_axioms_text = ''.join(bfo_axioms)
    return bfo_axioms_text


def prepare_clif_bfo(bfo_clif: str) -> str:
    fixed_bfo = __fix_quote_marks(bfo=bfo_clif)
    prepared_bfo = __extract_axioms(bfo=fixed_bfo)
    return prepared_bfo