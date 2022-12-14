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

print("====================")
print("If Else three condition")

g = 90000
h = 1000
print("benar") if g > h else print("Sama Nilainya") if g == h else print("Salah")

print("====================")
print("And The and keyword is a logical operator, and is used to combine conditional statements:")

i = 200
j = 33
k = 500

if i > j and k > i:
    print("Booth Condition are True")

print("====================")
print("Or The or keyword is a logical operator, and is used to combine conditional statements")

a = 200
b = 33
c = 500

if a > b or a > c:
    print("At Least one of the conditions is True")

print("=================")
print("Nested If")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.

x = 80

if x > 10:
    print("Above ten,")
    if x > 50:
        print("Also Above 50")
    else:
        print("But Not above 50")

print("===================")
print("Pass statement")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 90
b = 80
if a > b:
    pass
