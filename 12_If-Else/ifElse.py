"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals                  : a == b
Not Equals              : a != b
Less than               : a < b
Less than or equal to   : a <= b
Greater than            : a > b
Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""

print("if")
a = 900
b = 800

if a > b :
    print("a greather than b")

print("==============")

print("Elif The elif keyword is pythons way of saying if the previous conditions were not true, then try this condition")

a = 44
b = 44
if a > b:
    print("lebih besar nilai a")
elif a == b:
    print("Nilai A = nilai B")

print("=======================")

c = 900
d = 600

if c > d :
    print("Nilai c labih dari d")
elif c == d:
    print("nilai c = nilai d")
else:
    print("d lebih besar dari c")