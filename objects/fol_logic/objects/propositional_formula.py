from objects.fol_logic.objects.formula import Formula


class PropositionalFormula(Formula):
    def __init__(self, arguments: list, is_self_standing=False):
        super().__init__(is_self_standing=is_self_standing)
        self.arguments = arguments
        self.free_variables = self.get_free_variables()
        self.set_tptp_type()

    def get_free_variables(self) -> set:
        free_variables = set()
        for argument in self.arguments:
            if hasattr(argument, 'free_variables'):
                free_variables = free_variables.union(argument.free_variables)
        return free_variables
    
    def set_tptp_type(self):
        for argument in self.arguments:
            if argument.tptp_type == 'tff':
                self.tptp_type = 'tff'
                return
    
    def get_all_predicates(self) -> set:
        predicates = set()
        for argument in self.arguments:
            predicates = predicates.union(argument.get_all_predicates())
        return predicates

    def get_stronger_arguments(self, inverse_strength: bool) -> list:
        stronger_arguments = list()
        for argument in self.arguments:
            stronger_arguments.append(argument.make_stronger(inverse_strength))
        return stronger_arguments