from objects.fol_logic.objects.conjunction import Conjunction
from objects.fol_logic.objects.disjunction import Disjunction
from objects.fol_logic.objects.equivalence import Equivalence
from objects.fol_logic.objects.implication import Implication
from objects.fol_logic.objects.quantifying_formula import Quantifier

from bidict import bidict

WEAKER_STRONGER_BIMAP = (
    bidict(
        {
            Disjunction: Conjunction,
            Implication: Equivalence,
            Quantifier.EXISTENTIAL: Quantifier.UNIVERSAL
        }))