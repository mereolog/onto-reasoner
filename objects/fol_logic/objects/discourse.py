class Discourse(list):
    def __init__(self, predicates: list):
        super().__init__()
        self.extend(predicates)
        