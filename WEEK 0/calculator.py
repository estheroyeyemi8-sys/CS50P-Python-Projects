#INTEGERS $ FLOATS

x = int(input("What's x?"))
y = int(input("What's y?"))

z = x + y
print(z)


a = float(input("What's a?"))
b = float(input("What's b?"))



#Rouund up to the nearest whole number
c = round(a + b)

#Instead of print(c)
#To make it come out with a comma
print(f"{c:,}")



#Division in float
f= float(input("First number"))
g= float(input("Second number?"))

#To convert to 2 decimal place, use:
h= (f / g, 2)
print(h)
#OR
h = f/ g
print(f"{h: .2f}")