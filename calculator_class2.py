"""This Calculator class is designed to handle the most
common basic math functions that a traditional calculator
would handle. One extra method, show_expression(), was 
added as a way for the developer to test to see if the 
equations were being written correctly. In the future, 
more features may be added from the math module."""
import operator

class Calculator:
    def __init__(self):
        self.expression = []
    
    def push(self, item):
        self.item = str(item)
        if self.item != '=':
            self.expression.append(self.item)
    
    def equals(self):
        self.result = 0
        try:
            if self.result == 0:
                if self.expression[0].isdecimal():
                    d1 = int(self.expression[0])
                else:
                    d1 = float(self.expression[0])
            else:
                d1 = self.result
        
            if len(self.expression) > 1:
                if self.expression[-1].isdecimal():
                    d2 = int(self.expression[-1])
                else:
                    d2 = float(self.expression[-1])

        except ValueError:
            print()
            return 'Sorry, you started over, so you first need to enter an integer or float!'

        operation = self.expression[1]
        ops = {'**':operator.pow(d1, d2), '*':operator.mul(d1, d2), '/':operator.truediv(d1, d2),
        '//':operator.floordiv(d1, d2), '+':operator.add(d1, d2), '-':operator.sub(d1, d2)}
        
        try:
            self.result = ops[operation]
            self.expression = ' '.join(self.expression).strip()
            return f'{self.expression} = {self.result}'.lstrip()
        
        except KeyError:
            self.clear()
            print()
            return 'Oops, you did not enter a valid operator. Please start again and check your equation carefully!'
        
        except ValueError:
            self.clear()
            print()
            return 'Sorry, you need at least two numbers to perform an operation. Please start over again.'
        
            
    
    def clear(self):
        self.expression = []
    
    def show_expression(self):
        return self.expression




