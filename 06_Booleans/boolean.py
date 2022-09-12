"""
Boolean Values
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""

from tkinter.font import BOLD


print(10 < 9)
print(10 == 7)
print(10 > 9)

#  run a condition in an if statement, Python returns True or False:

a = 300
b = 90

if b > a:
    print("90 lebih besar dari 300")
else:
    print("90 TIDAK lebih besar dari 300")

# Evaluate Values and Variables The bool() 
# #function allows you to evaluate any value, and give you True or False in return,

print(bool("Hello"))
print(bool(89))