print("hello world")
emeka = 5
tobi = 2
z = " Five is greater than 2 "
if emeka > tobi:
    print(z)


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print(10 > 9 and 10 > 11)

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist.insert(1, "pineapple")
thislist.append("Guava")
for x in thislist:
  print(x)
