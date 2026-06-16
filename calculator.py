class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        temp=0
        temp2=0
        temp3=0
        temp4=0
        temp5=0
       
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b
