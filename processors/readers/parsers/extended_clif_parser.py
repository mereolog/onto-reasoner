import ply.lex as lex
import ply.yacc as yacc

from objects.fol_logic.objects.atomic_formula import AtomicFormula
from objects.fol_logic.objects.conjunction import Conjunction
from objects.fol_logic.objects.disjunction import Disjunction
from objects.fol_logic.objects.equivalence import Equivalence
from objects.fol_logic.objects.function_term import FunctionSymbol
from objects.fol_logic.objects.identity_formula import IdentityFormula
from objects.fol_logic.objects.implication import Implication
from objects.fol_logic.objects.indiscourse import Indiscourse
from objects.fol_logic.objects.negation import Negation
from objects.fol_logic.objects.outdiscourse import Outdiscourse
from objects.fol_logic.objects.predicate import Predicate
from objects.fol_logic.objects.quantifying_formula import QuantifyingFormula, Quantifier
from objects.fol_logic.objects.term import Term
from objects.fol_logic.objects.theory import Theory
from objects.fol_logic.objects.variable import Variable

tokens = \
    [
        'OPEN',
        'CLOSE',
        'STRINGQUOTE',
        'NAMEQUOTE',
        'BACKSLASH',
        'CHAR',
        'HEXA',
        'INNERSTRINGQUOTE',
        'INNERNAMEQUOTE',
        'INNERBACKSLASH',
        'NUMERAL',
        'SEQMARK',
        'QUOTEDSTRING',
        'ENCLOSEDNAME',
        'NAMECHARSEQUENCE',
        'ID'
    ]

reserved = {
    "=": 'EQUAL',
    'and': 'AND',
    'or': 'OR',
    'iff': 'IFF',
    'if': 'IF',
    'forall': 'FORALL',
    'exists': 'EXISTS',
    'not': 'NOT',
    'cl:text': 'TEXT',
    'cl:ttl': 'TITLING',
    'cl:imports': 'IMPORTS',
    'cl:restrict': 'RESTRICT',
    'cl:indiscourse': 'INDISCOURSE',
    'cl:outdiscourse': 'OUTDISCOURSE',
    'cl:comment': 'COMMENT',
    'cl:prefix': 'PREFIX'
}

tokens += reserved.values()

literals = ['(', ')']


def t_NUMERAL(t):
    r'[0-9]+'
    return t


def t_SEQMARK(t):
    r'\.\.\.'
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_OPEN = r'\('
t_CLOSE = r'\)'
t_STRINGQUOTE = r"'"
t_NAMEQUOTE = r'"'
t_BACKSLASH = r'\\'
t_CHAR = r'[A-Za-z0-9~\!#$%^&\*_\+\{\}\|:<>\?\-\[\];,\./=]'
t_HEXA = r'[0-9ABCDEF]'
t_INNERSTRINGQUOTE = r"\\'"
t_INNERNAMEQUOTE = r'\\"'
t_INNERBACKSLASH = r'\\\\'

t_ignore = ' \t\r\n\f\v'

t_QUOTEDSTRING = (
        t_STRINGQUOTE +
        '(' + r'\s' + ' | ' + t_OPEN + ' | ' + t_CLOSE + ' | ' + t_CHAR + ' | ' + t_NAMEQUOTE + ' | ' + t_INNERSTRINGQUOTE + ' | ' + t_INNERBACKSLASH + ')+' +
        t_STRINGQUOTE)

t_ENCLOSEDNAME = (
        t_NAMEQUOTE +
        '(' + r'\s' + ' | ' + t_OPEN + ' | ' + t_CLOSE + ' | ' + t_CHAR + ' | ' + t_STRINGQUOTE + ' | ' + t_INNERNAMEQUOTE + ')+' +
        t_NAMEQUOTE)

t_NAMECHARSEQUENCE = (
        t_CHAR + '(' + t_CHAR + ' | ' + t_STRINGQUOTE + ' | ' + t_NAMEQUOTE + ' | ' + t_BACKSLASH + ')*')


def t_RESERVED(t):
    r'=\s+|not\s+|and\s+|or\s+|iff\s+|if\s+|forall\s+|exists\s+|cl:text\s+|cl:ttl\s+|cl:imports\s+|cl:restrict\s+|cl:imports\s+|cl:indiscourse\s+|cl:outdiscourse\s+|cl:comment\s+|cl:prefix\s+'
    t.value = t.value.strip()
    t.type = reserved.get(t.value)
    return t


def p_extended_texts(p):
    """
    extended_text : texts
        | statements
        | sentences
    """
    p[0] = p[1]

def p_texts(p):
    """
    texts : text texts
    texts : text
    """
    if len(p) == 3:
        texts = [p[1]]
        if isinstance(p[2], list):
            texts += p[2]
        else:
            texts.append(p[2])
        p[0] = texts
    else:
        p[0] = p[1]


def p_text(p):
    """
    text : textconstruction
        | domainrestriction
        | importation
        | commenttext
    """
    if isinstance(p[1], Theory):
        p[0] = p[1]
    else:
        p[0] = Theory(parts=p[1])


def p_textconstruction(p):
    """
    textconstruction : OPEN TEXT constructed_texts CLOSE
    """
    p[0] = p[3]


def p_constructed_texts(p):
    """
    constructed_texts : constructed_text constructed_texts
    constructed_texts : constructed_text
    """
    if len(p) == 3:
        constructed_texts = [p[1]]
        if isinstance(p[2], list):
            constructed_texts += p[2]
        else:
            constructed_texts.append(p[2])
        p[0] = constructed_texts
    else:
        p[0] = p[1]


def p_constructed_text(p):
    """
    constructed_text    : sentence
                        | statement
                        | text
    """
    p[0] = p[1]


def p_statements(p):
    """
    statements : statement statements
    statements : statement
    """
    if len(p) == 3:
        statements = [p[1]]
        if isinstance(p[2], list):
            statements += p[2]
        else:
            statements.append(p[2])
        p[0] = statements
    else:
        p[0] = [p[1]]


def p_statement(p):
    """
    statement : titling
    statement : discoursestatement
    statement : OPEN COMMENT QUOTEDSTRING statement CLOSE
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[4]


def p_discoursestatement(p):
    """
    discoursestatement  : indiscourse
                        | outdiscourse
    """
    p[0] = p[1]


def p_indiscourse(p):
    """
    indiscourse : OPEN INDISCOURSE terms CLOSE
    """
    p[0] = Indiscourse(predicates=p[3])


def p_outdiscourse(p):
    """
    outdiscourse : OPEN OUTDISCOURSE terms CLOSE
    """
    p[0] = Outdiscourse(predicates=p[3])


def p_domainrestriction(p):
    """
    domainrestriction : OPEN RESTRICT term text CLOSE
    """
    p[0] = p[4]


def p_importation(p):
    """
    importation : OPEN IMPORTS interpretablename CLOSE
    """
    p[0] = p[3]


def p_commenttext(p):
    """
    commenttext : OPEN COMMENT QUOTEDSTRING texts CLOSE
    commenttext : OPEN COMMENT QUOTEDSTRING prefixdeclarations texts CLOSE
    """
    if len(p) == 6:
        if isinstance(p[4], list):
            for theory in p[4]:
                theory.comment = p[3]
        else:
            p[4].comment = p[3]
        p[0] = p[4]
    else:
        if isinstance(p[5], list):
            for theory in p[5]:
                theory.comment = p[3]
        else:
            p[5].comment = p[3]
        p[0] = p[5]


def p_prefixdeclarations(p):
    """
    prefixdeclarations : prefixdeclaration prefixdeclarations
    prefixdeclarations : prefixdeclaration
    """
    if len(p) == 3:
        prefixdeclarations = [p[1]]
        if isinstance(p[2], list):
            prefixdeclarations += p[2]
        else:
            prefixdeclarations.append(p[2])
        p[0] = prefixdeclarations
    else:
        p[0] = [p[1]]


def p_prefixdeclaration(p):
    """
    prefixdeclaration : OPEN PREFIX QUOTEDSTRING interpretablename CLOSE
    """
    p[0] = p[4]


def p_titling(p):
    """
    titling : OPEN TITLING interpretablename text CLOSE
    """
    p[0] = p[4]


def p_sentence(p):
    """
    sentence :  atomsent
        | boolsent
        | existential_quantsent
        | universal_quantsent
        | commentsent
    """
    p[0] = p[1]


def p_atomsent(p):
    """
    atomsent :  equation
        | atom
    """
    p[0] = p[1]


def p_boolsent(p):
    """
    boolsent : and_sent
        | or_sent
        | if_sent
        | iff_sent
        | not_sent
    """
    p[0] = p[1]


def p_and_sent(p):
    """
    and_sent : OPEN AND sentences CLOSE
    """
    arguments = p[3]
    p[0] = Conjunction(arguments=arguments)


def p_or_sent(p):
    """
    or_sent : OPEN OR sentences CLOSE
    """
    arguments = p[3]
    p[0] = Disjunction(arguments=arguments)


def p_if_sent(p):
    """
    if_sent : OPEN IF sentence sentence CLOSE
    """
    p[0] = Implication(arguments=[p[3], p[4]])


def p_iff_sent(p):
    """
    iff_sent : OPEN IFF sentence sentence CLOSE
    """
    p[0] = Equivalence(arguments=[p[3], p[4]])


def p_not_sent(p):
    """
    not_sent : OPEN NOT sentence CLOSE
    """
    p[0] = Negation(arguments=[p[3]])


def p_commentsent(p):
    """
    commentsent : OPEN COMMENT QUOTEDSTRING sentence CLOSE
    """
    p[4].comment = p[3]
    p[0] = p[4]


def p_sentences(p):
    """
    sentences : sentence sentences
    sentences : sentence
    """
    if len(p) == 3:
        sentences = [p[1]]
        if isinstance(p[2], list):
            sentences += p[2]
        else:
            sentences.append(p[2])
        p[0] = sentences
    else:
        p[0] = [p[1]]


def p_equation(p):
    """
    equation : OPEN EQUAL term term CLOSE
    """
    arguments = [Variable(letter=p[3]), Variable(letter=p[4])]
    p[0] = IdentityFormula(arguments=arguments)


def p_atom(p):
    """
    atom : OPEN term termseq CLOSE
    """
    arguments = list()
    for term in p[3]:
        if isinstance(term, str):
            argument = Variable(letter=term)
        else:
            argument = term
        arguments.append(argument)
    p[0] = AtomicFormula(predicate=Predicate(origin_value=p[2], arity=len(arguments)), arguments=arguments)


def p_universal_quantsent(p):
    """
    universal_quantsent : OPEN FORALL OPEN bvar_list CLOSE sentence CLOSE
    """
    variables = list()
    for term in p[4]:
        if isinstance(term, str):
            variable = Variable(letter=term)
        else:
            variable = term
        variables.append(variable)
    p[0] = QuantifyingFormula(quantified_formula=p[6], bound_variables=variables, quantifier=Quantifier.UNIVERSAL)


def p_existential_quantsent(p):
    """
    existential_quantsent : OPEN EXISTS OPEN bvar_list CLOSE sentence  CLOSE
    """
    variables = list()
    for term in p[4]:
        if isinstance(term, str):
            variable = Variable(letter=term)
        else:
            variable = term
        variables.append(variable)
    p[0] = QuantifyingFormula(quantified_formula=p[6], bound_variables=variables, quantifier=Quantifier.EXISTENTIAL)


def p_bvar_list(p):
    """
    bvar_list : bvar bvar_list
        | bvar
    """
    if len(p) == 3:
        bvars = [p[1]]
        if isinstance(p[2], list):
            bvars += p[2]
        else:
            bvars.append(p[2])
        p[0] = bvars
    else:
        p[0] = [p[1]]


def p_bvar(p):
    """
    bvar : interpretablename
        | cseqmark
        | OPEN interpretablename term CLOSE
        | OPEN cseqmark term CLOSE
    """
    p[0] = p[1]


def p_terms(p):
    """
    terms : term terms
    terms : term
    """
    if len(p) == 3:
        terms = [p[1]]
        if isinstance(p[2], list):
            terms += p[2]
        else:
            terms.append(p[2])
        p[0] = terms
    else:
        p[0] = [p[1]]


def p_termseq(p):
    """
    termseq : termseq term
        | termseq SEQMARK
        | term
        | SEQMARK
    """
    if len(p) == 2:
        p[0] = [p[1]]
    if len(p) == 3:
        p[0] = [term for term in p[1]]
        p[0].append(p[2])


def p_term(p):
    """
    term : name
        | OPEN term termseq CLOSE
        | OPEN COMMENT QUOTEDSTRING term CLOSE
    """
    if len(p) == 2:
        Term(origin_value=p[1])
        p[0] = p[1]
    if len(p) == 5:
        function_term = Term(origin_value=p[2])
        arguments = [Term(origin_value=parameter) for parameter in p[3]]
        p[0] = FunctionSymbol(origin_value=p[2], term=function_term, arguments=arguments)
    if len(p) == 6:
        Term(origin_value=p[4])
        p[0] = p[4]


def p_name(p):
    """
    name : interpretedname
        | interpretablename
    """
    p[0] = p[1]


def p_interpretedname(p):
    """
    interpretedname : NUMERAL
        | QUOTEDSTRING
        | OPEN COMMENT QUOTEDSTRING NUMERAL CLOSE
        | OPEN COMMENT QUOTEDSTRING QUOTEDSTRING CLOSE
    """
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 6:
        p[0] = p[4]


def p_interpretablename(p):
    """
    interpretablename : NAMECHARSEQUENCE
        | ENCLOSEDNAME
        | OPEN COMMENT QUOTEDSTRING interpretablename CLOSE
    """
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 6:
        p[0] = p[4]


def p_cseqmark(p):
    """
    cseqmark : SEQMARK
        | OPEN COMMENT QUOTEDSTRING SEQMARK CLOSE
    """
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 6:
        p[0] = p[4]


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def p_error(p):
    print("Syntax error in input!")


def extended_parse_clif(text: str):
    # logging.info(msg='Parsing')
    lexer = lex.lex()
    parser = yacc.yacc()
    lexer.input(text)
    parseds = parser.parse(text)
    return parseds
    
