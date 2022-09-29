"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""
# lamda arguments : expression

from regex import B


x = lambda a : a + 10
print(x(9))

# lamda multi Argument

x = lambda a, b : a + b
print(x(5, 6))

# Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(4,5,6))