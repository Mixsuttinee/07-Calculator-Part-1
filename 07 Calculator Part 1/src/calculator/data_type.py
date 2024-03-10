"""Data type for the calculator"""
from calculator.factorial import factorial

class Number:
    

    def __init__(self, value):
        self.value = value

    def execute(self):
        return self.value
    
class FactorialTerm:
    

    def __init__(self, operand):
        self.operand = operand

    def execute(self):
        return factorial(self.operand.execute())
    
class PowerTerm:
    

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def execute(self):
        return self.left.execute() ** self.right.execute()
    
class UnaryTerm:
    

    def __init__(self, operator, operand):
        self.operand = operand
        self.operator = operator

    def execute(self):
        if self.operator == "-":
            return - self.operand.execute()
        else : 
            return self.operand.execute()
        
class MulExpr:
    
    def __init__(self, operator,left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def execute(self):
        if self.operator == "*":
            return self.left.execute() * self.right.execute()
        elif self.operator == "/":
            return self.left.execute() / self.right.execute()
        elif self.operator == "%":
            return self.left.execute() % self.right.execute()
        else : raise ValueError("Unrecognized operator")

class AddExpr:
    
    def __init__(self, operator,left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def execute(self):
        if self.operator == "+":
            return self.left.execute() + self.right.execute()
        elif self.operator == "-":
            return self.left.execute() - self.right.execute()
        else : raise ValueError("Unrecognized operator")

class Pimary():
    pass