import re
txt = input(" Enter your text: ")
scr = input(" Ennter what you want to search for : ")
replace = input(" Enter what you want to replace with ")
def regular_text(text,srch,replace):
    # print(text,srch,replace)
    # x = re.search(srch, text)
    # if x == True:
    y = len(re.findall(srch, text))
    if y != 0:
        # print(y)
        xy = re.sub(srch, replace, text)
        print(xy)
    else:
        print(" not available " + str(y))    
    
regular_text(txt, scr, replace)