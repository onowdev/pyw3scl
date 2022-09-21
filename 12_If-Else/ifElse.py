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
    print("Nilai c lebih dari d")
elif c == d:
    print("nilai c = nilai d")
else:
    print("d lebih besar dari c")

print("===================")
print("Short Hand If If you have only one statement to execute, you can put it on the same line as the if statement.")

if 8000 > 900:print("8000 itu lebih besar dari 900")

print("===================")
print("Short Hand If ... Else If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:")

e = 90
f = 80
print("Benar") if e > f else print("Salah")