import random
class paren:
    def __init__(self,mommyname,daddyname):
        self.mommyname = mommyname
        self.daddyname = daddyname
        
    def childrencount(self):
        self.childrencountnumber = random.randrange(1, 10)
        return self.childrencountnumber
    

# myparent = paren('mommy','emaka')

# children = myparent.childrencount()
# print(myparent.mommyname + " "+ myparent.daddyname)
# print(children)    