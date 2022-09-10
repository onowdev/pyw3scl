"""
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
Example :
"""

print("integer cating")
a = int(9)
b = int(7.8)
c = int("90")

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

print("Float Casting")
d = float(9.89)
e = float(8)
f = float("898")
g = float("9.89")
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))

print("string casting")

k = str("90abc")
l = str(9.89)
m = str(789)

print(type(k))
print(type(l))
print(type(m))