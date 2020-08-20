operand1 = input(" Enter Operations: ")
# operand2 = int(input(" Enter Operand 2: "))
# operate= input(" Enter operation desired example + , - ")
result = 0
num1 = 0
num2 = 0
class calculator:
    def add(self, num1,num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multipy(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 / num2
    
mycalc = calculator()    
op = operand1.split()
print(op)