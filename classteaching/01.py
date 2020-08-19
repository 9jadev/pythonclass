# class Car:
#     def __init__(self, tyre):
#         self.tyre = 4
    
    
# benz = Car() 

# benztyres = benz.tyre
# print(benztyres)

class Thermometerdiff:
    
    def celcius_to_kelvin(self, amount):    
        result = amount + 273
        return result
    def kelvin_to_celcius(self, amount):
        result = amount - 273
        return result
    
thermometer = Thermometerdiff() 
convert1 = thermometer.celcius_to_kelvin(120)
convert2 = thermometer.kelvin_to_celcius(2938)
print(convert2)