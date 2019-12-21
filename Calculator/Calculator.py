from Calculator.Addition import Addition
from Calculator.Subtraction import Subtraction
from Calculator.Multiplication import Multiplication
from Calculator.Division import Division
from Calculator.Square import Square
from Calculator.Squareroot import Squareroot



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
    
     def substract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
    
     def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result
    
     def divide(self, a, b):
        self.result = division(a, b)
        return self.result
    
     def square(self, a, b):
        self.result = square(a, b)
        return self.result
    
     def squartroot(self, a, b):
        self.result = squareroot(a, b)
        return self.result
