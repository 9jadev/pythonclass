import paren 
getmom = input(" Give us moms name: ")
getdad = input(" Give us dads name: ")
class omo(paren.paren):
    def __init__(self):
        super().__init__(getmom,getdad)
    
omo = omo()
# print(paren.paren.childrencount(self))
print(omo.childrencount())
print(omo.daddyname+ " " +omo.mommyname)