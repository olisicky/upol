# ObjektovĂĄ implementace spojovĂ˝ch seznamĹŻ
#
# Definuje konstanu empty pro prĂĄzdnĂ˝ seznam
# a funkce:
# - cons(val, lst) ... pĹidĂĄnĂ­ prvku k seznamu
# - first(lst) ... prvnĂ­ prvek neprĂĄzdnĂŠho seznamu
# - rest(lst) ... zbytek neprĂĄzdnĂŠho seznamu
# - is_empty(lst) ... rozhoduje, zda je seznam prĂĄzdnĂ˝.

class List:
    pass

class Empty(List):
    def is_empty(self):
        return True
    
    def __repr__(self):
        return "empty"

empty = Empty()

class NonEmpty(List):
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def get_first(self):
        return self.first

    def get_rest(self):
        return self.rest

    def is_empty(self):
        return False
    
    def __repr__(self):
        return ("cons("
                + repr(self.get_first())
                + ", "
                + repr(self.get_rest())
                + ")")

    def __eq__(self, val):
        return (isinstance(val, NonEmpty)
                and self.get_first() == val.get_first()
                and self.get_rest() == val.get_rest())


# Konstruktor:
def cons(val, lst):
    return NonEmpty(val, lst)

# Selektory:
def first(lst):
    return lst.get_first()

def rest(lst):
    return lst.get_rest()

# Test prĂĄzdnosti:
def is_empty(lst):
    return lst.is_empty()