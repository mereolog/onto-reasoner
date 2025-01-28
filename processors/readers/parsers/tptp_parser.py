
import ply.lex as lex
import ply.yacc as yacc

from objects.fol_logic.objects.atomic_formula import AtomicFormula
from objects.fol_logic.objects.conjunction import Conjunction
from objects.fol_logic.objects.disjunction import Disjunction
from objects.fol_logic.objects.equivalence import Equivalence
from objects.fol_logic.objects.formula import Formula
from objects.fol_logic.objects.identity_formula import IdentityFormula
from objects.fol_logic.objects.implication import Implication
from objects.fol_logic.objects.negation import Negation
from objects.fol_logic.objects.predicate import Predicate
from objects.fol_logic.objects.quantifying_formula import QuantifyingFormula, Quantifier
from objects.fol_logic.objects.variable import Variable

# List of token names
tokens = (
    'FOF',
    'NAME',
    'FORMULA_ROLE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'DOT',
    'COLON',
    'EXCLAMATION',
    'QUESTION',
    'EQUIVALENT',
    'IMPLIES',
    'REVERSE_IMPLIES',
    'NOT_EQUIVALENT',
    'OR',
    'AND',
    'NOT',
    'VARIABLE',
    'CONSTANT',
    'DEFINED_CONSTANT',
    'SYSTEM_CONSTANT',
    'SINGLE_QUOTED',
    'DEFINED_INFIX_PRED',
    'INFIX_INEQUALITY',
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_EXCLAMATION = r'!'
t_QUESTION = r'\?'
t_EQUIVALENT = r'<=>'
t_IMPLIES = r'=>'
t_REVERSE_IMPLIES = r'<='
t_NOT_EQUIVALENT = r'<~>'
t_OR = r'\|'
t_AND = r'&'
t_NOT = r'~'
t_DEFINED_INFIX_PRED = r'='  # Example for defined infix predicate
t_INFIX_INEQUALITY = r'!='   # Example for infix inequality

t_ignore = ' \t\r\n\f\v'

# Regular expression rules with some action code
def t_FOF(t):
    r'fof'
    return t

def t_FORMULA_ROLE(t):
    r'\baxiom\b|\bhypothesis\b|\bdefinition\b|\bassumption\b|\blemma\b|\btheorem\b|\bcorollary\b|\bconjecture\b|\bnegated_conjecture\b|\bplain\b|\btype\b|\binterpretation\b|\bfi_domain\b|\bfi_functors\b|\bfi_predicates\b|\bunknown\b'
    return t

def t_NAME(t):
    r'TPTP_FORMULA'
    # r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_VARIABLE(t):
    r'[A-Z][a-zA-Z_0-9]*'
    return t

def t_CONSTANT(t):
    r'[a-z][a-zA-Z_0-9]*'
    return t

def t_DEFINED_CONSTANT(t):
    r'\$[a-zA-Z_0-9]+'
    return t

def t_SYSTEM_CONSTANT(t):
    r'\$\$[a-zA-Z_0-9]+'
    return t

def t_SINGLE_QUOTED(t):
    r"'([^\\']|\\.)*'"
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_tptp_theory(p):
    """
    tptp_theory : annotated_formula tptp_theory
    tptp_theory : annotated_formula
    """
    if len(p) == 3:
        theory = [p[1]]
        if isinstance(p[2], list):
            theory += p[2]
        else:
            theory.append(p[2])
        p[0] = theory
    else:
        p[0] = [p[1]]

def p_annotated_formula(p):
    """annotated_formula : fof_annotated"""
    p[0] = p[1]

def p_fof_annotated(p):
    """fof_annotated : FOF LPAREN NAME COMMA FORMULA_ROLE COMMA fof_formula RPAREN DOT"""
    if isinstance(p[7],Formula):
        p[7].comment = p[3]
    p[0] = p[7]

def p_fof_formula(p):
    """fof_formula : fof_logic_formula"""
    p[0] = p[1]

def p_fof_logic_formula(p):
    """fof_logic_formula : fof_binary_formula
                         | fof_unary_formula
                         | fof_unitary_formula"""
    p[0] = p[1]

def p_fof_binary_formula(p):
    """fof_binary_formula : fof_binary_nonassoc
                          | fof_binary_assoc"""
    p[0] = p[1]

def p_fof_binary_nonassoc(p):
    """fof_binary_nonassoc : fof_unit_formula nonassoc_connective fof_unit_formula"""
    if p[2] == t_AND:
        p[0] = Conjunction(arguments=[p[1], p[3]])
    if p[2] == t_OR:
        p[0] = Disjunction(arguments=[p[1], p[3]])
    if p[2] == t_IMPLIES:
        p[0] = Implication(arguments=[p[1], p[3]])
    if p[2] == t_EQUIVALENT:
        p[0] = Equivalence(arguments=[p[1], p[3]])

def p_fof_unit_formula(p):
    """fof_unit_formula : fof_unitary_formula
                        | fof_unary_formula"""
    p[0] = p[1]

def p_fof_unitary_formula(p):
    """fof_unitary_formula : fof_quantified_formula
                           | fof_atomic_formula
                           | LPAREN fof_logic_formula RPAREN"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_fof_quantified_formula(p):
    """fof_quantified_formula : fof_quantifier LBRACKET fof_variable_list RBRACKET COLON fof_unit_formula"""
    if p[1] == t_EXCLAMATION:
        quantifier = Quantifier.UNIVERSAL
    else:
        quantifier = Quantifier.EXISTENTIAL
    p[0] = QuantifyingFormula(quantified_formula=p[6],quantifier=quantifier,bound_variables=p[3])

def p_fof_variable_list(p):
    """fof_variable_list : variable
                         | variable COMMA fof_variable_list"""
    if len(p) == 4:
        arguments = [p[1]]
        if isinstance(p[3], list):
            arguments += p[3]
        else:
            arguments.append(p[3])
        p[0] = arguments
    else:
        p[0] = [p[1]]

def p_fof_atomic_formula(p):
    """fof_atomic_formula : fof_plain_atomic_formula
                          | fof_defined_atomic_formula
                          | fof_system_atomic_formula"""
    p[0] = p[1]

def p_fof_plain_atomic_formula(p):
    """fof_plain_atomic_formula : fof_plain_term"""
    p[0] = p[1]

def p_fof_defined_atomic_formula(p):
    """fof_defined_atomic_formula : fof_defined_plain_formula
                                  | fof_defined_infix_formula"""
    p[0] = p[1]

def p_fof_defined_plain_formula(p):
    """fof_defined_plain_formula : fof_defined_plain_term"""
    p[0] = p[1]

def p_fof_defined_infix_formula(p):
    """fof_defined_infix_formula : fof_term DEFINED_INFIX_PRED fof_term"""
    p[0] = IdentityFormula(arguments=[p[1], p[3]])

def p_fof_quantifier(p):
    """fof_quantifier : EXCLAMATION
                      | QUESTION"""
    p[0] = p[1]

def p_nonassoc_connective(p):
    """nonassoc_connective : EQUIVALENT
                           | IMPLIES
                           | REVERSE_IMPLIES
                           | NOT_EQUIVALENT"""
    p[0] = p[1]

def p_unary_connective(p):
    """unary_connective : NOT"""
    p[0] = p[1]

def p_variable(p):
    """variable : VARIABLE"""
    p[0] = Variable(letter=p[1])

def p_fof_plain_term(p):
    """fof_plain_term : constant
                      | functor LPAREN fof_arguments RPAREN"""
    if len(p) == 2:
        p[0] = Variable(letter=p[1])
    else:
        p[0] = (
            AtomicFormula(
                predicate=Predicate(origin_value=p[1],arity=len(p[3])),
                arguments=p[3],
                origin_type='tptp'))

def p_constant(p):
    """constant : CONSTANT"""
    p[0] = p[1]

def p_functor(p):
    """functor : atomic_word"""
    p[0] = p[1]

def p_atomic_word(p):
    """atomic_word : lower_word
                   | single_quoted"""
    p[0] = p[1]

def p_lower_word(p):
    """lower_word : CONSTANT"""
    p[0] = p[1]

def p_single_quoted(p):
    """single_quoted : SINGLE_QUOTED"""
    p[0] = p[1]

def p_fof_unary_formula(p):
    """fof_unary_formula : unary_connective fof_unit_formula
                         | fof_infix_unary"""
    if len(p) == 3:
        p[0] = Negation(arguments=[p[2]])
    else:
        p[0] = p[1]

def p_fof_infix_unary(p):
    """fof_infix_unary : fof_term INFIX_INEQUALITY fof_term"""
    p[0] = p[1]

def p_fof_term(p):
    """fof_term : fof_function_term
                | variable"""
    p[0] = p[1]

def p_fof_function_term(p):
    """fof_function_term : fof_plain_term
                         | fof_defined_term
                         | fof_system_term"""
    p[0] = p[1]

def p_fof_defined_term(p):
    """fof_defined_term : fof_defined_atomic_term"""
    p[0] = p[1]

def p_fof_defined_atomic_term(p):
    """fof_defined_atomic_term : fof_defined_plain_term"""
    p[0] = p[1]

def p_fof_defined_plain_term(p):
    """fof_defined_plain_term : defined_constant
                              | defined_functor LPAREN fof_arguments RPAREN"""
    p[0] = p[1]

def p_defined_constant(p):
    """defined_constant : defined_functor"""
    p[0] = p[1]

def p_defined_functor(p):
    """defined_functor : atomic_defined_word"""
    pass

def p_atomic_defined_word(p):
    """atomic_defined_word : dollar_word"""
    pass

def p_dollar_word(p):
    """dollar_word : DEFINED_CONSTANT"""
    pass

def p_fof_arguments(p):
    """fof_arguments : fof_term
                     | fof_term COMMA fof_arguments"""

    if len(p) == 4:
        arguments = [p[1]]
        if isinstance(p[3], list):
            arguments += p[3]
        else:
            arguments.append(p[3])
        p[0] = arguments
    else:
        p[0] = [p[1]]

def p_fof_system_atomic_formula(p):
    """fof_system_atomic_formula : fof_system_term"""
    pass

def p_fof_system_term(p):
    """fof_system_term : system_constant
                       | system_functor LPAREN fof_arguments RPAREN"""
    pass

def p_system_constant(p):
    """system_constant : SYSTEM_CONSTANT"""
    pass

def p_system_functor(p):
    """system_functor : atomic_system_word"""
    pass

def p_atomic_system_word(p):
    """atomic_system_word : dollar_dollar_word"""
    pass

def p_dollar_dollar_word(p):
    """dollar_dollar_word : SYSTEM_CONSTANT"""
    pass

def p_fof_binary_assoc(p):
    """fof_binary_assoc : fof_or_formula
                        | fof_and_formula"""
    p[0] = p[1]

def p_fof_or_formula(p):
    """fof_or_formula : fof_unit_formula OR fof_unit_formula
                      | fof_or_formula OR fof_unit_formula"""
    p[0] = Disjunction(arguments=[p[1], p[3]])

def p_fof_and_formula(p):
    """fof_and_formula : fof_unit_formula AND fof_unit_formula
                       | fof_and_formula AND fof_unit_formula"""
    p[0] = Conjunction(arguments=[p[1], p[3]])

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


def parse_tptp(text: str):
    lexer = lex.lex()
    parser = yacc.yacc()
    lexer.input(text)
    parsed_text = parser.parse(text)
    return parsed_text