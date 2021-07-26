class Prototype:
    def clone(self):
        import copy
        return copy.deepcopy(self)