operand1 = int(input(" Enter Operand 1: "))
operand2 = int(input(" Enter Operand 2: "))
result  = 0
operate= input(" Enter operation desired example + , - ")

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

if operate == "+":
    addition = mycalc.add(operand1,operand2)
    # print(addition)
    result = addition
     
if operate == "-":
    subtraction = mycalc.subtract(operand1,operand2)
    # print(subtraction)
    result = subtraction
    
if operate == "*":
    multiplication = mycalc.multipy(operand1,operand2)
    result = multiplication 
if operate == "/":
    division = mycalc.divide(operand1,operand2)
    result = division         
       
while True:
    uper = input("new operation")
    if uper == "=":
        print(result)
        break
    num2 = int(input("new number"))   
    if uper == "+":
        addition = mycalc.add(result,num2)
        # print(addition)
        result = addition
        
    if uper == "-":
        subtraction = mycalc.subtract(result,num2)
        # print(subtraction)
        result = subtraction
        
    if uper == "*":
        multiplication = mycalc.multipy(result,num2)
        # print(multiplication) 
        result = addition
    if uper == "/":
        division = mycalc.divide(result,num2)
        # print(division)
        result = addition
        
     

    



    