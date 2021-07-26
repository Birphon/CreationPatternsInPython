class Prototype(object):
    def clone(self):
        import copy
        return copy.deepcopy(self)