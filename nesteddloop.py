multipler = range(1, 101)

for x in multipler:
    f = open("demofile2.txt", "a")
    f.write(" \n Table for " + str(x) )
    print(" \n Table for " + str(x) )
    for y in range(1,13):
        result = x*y
        f.write("\n" +  str(x) + "X" + str(y) + "=" + str(result) )
        print(str(x) + "X" + str(y) + "=" + str(result))
