class Prop:
    def __str__(self):
        return self.__repr__()

class Atom(Prop):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class Not(Prop):
    def __init__(self, operand):
        self.operand = operand
    def __repr__(self):
        return f"¬({self.operand})"

class And(Prop):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __repr__(self):
        return f"({self.left} ∧ {self.right})"

class Box(Prop):  # □ necessity
    def __init__(self, operand):
        self.operand = operand
    def __repr__(self):
        return f"□({self.operand})"

class Diamond(Prop):  # ◇ possibility
    def __init__(self, operand):
        self.operand = operand
    def __repr__(self):
        return f"◇({self.operand})"

# Example usage
# p = Atom("p")
# q = Atom("q")
# formula = Box(And(p, q))  # □(p ∧ q)
# print(formula)
