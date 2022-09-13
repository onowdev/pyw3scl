"""
Python Operators
Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

    > Arithmetic operators
    > Assignment operators
    > Comparison operators
    > Logical operators
    > Identity operators
    > Membership operators
    > Bitwise operators

"""
print("====================")
print("Arithmetic Operators")
print("====================")
a = 9
b = 8
print("Addition", a+b)
print("Subtraction", a-b)
print("Multiplication", a * b)
print("Division", a / b)
print("Modulus", a % b)
print("Exponentiation", a ** 3)
print("Floor division", a // b)

print("====================")
print("Assignment Operators")
print("====================")

x = 9
print(x)

x+= 8
print(x)

x-= 7
print(x)

x*=2
print(x)

x/=2
print(x)

x%=3
print(x)

print("=====================")
print("Comparision Operators")
print("=====================")

c = 900
d = 825

print("Equal is", c==d)
print("Not Equal is", c != d)
print("Greater Than", c > d)
print("Less than", c < d)
print("Greater than or equal to",c >= d)
print("Less Than or Equal to", c<=d)