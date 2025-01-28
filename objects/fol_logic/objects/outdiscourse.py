from objects.fol_logic.objects.discourse import Discourse

class Outdiscourse(Discourse):
    def __init__(self, predicates: list):
        super().__init__(predicates)
        