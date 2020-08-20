# class Car:
#     def __init__(self, tyre):
#         self.tyre = 4
    
    
# benz = Car() 

# benztyres = benz.tyre
# print(benztyres)

scalefrom = input(" Enter present Scale: ")
scaleto = input(" Enter changing scale ")
amount = int(input("Enter amount"))

class Thermometerdiff:
    
    def celcius_to_kelvin(self, amount):    
        result = amount + 273
        return result
    def kelvin_to_celcius(self, amount):
        result = amount - 273
        return result
    
thermometer = Thermometerdiff() 
 
 if scalefrom == 'celcius' and scaleto == 'kelvin':
    convert1 = thermometer.celcius_to_kelvin(120)
    print(convert1)


convert2 = thermometer.kelvin_to_celcius(2938)
print(convert2)