"""
Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

"""

# Upper Case
a = "hello, world! my friend"
print(a.upper())

# LowerCase

b = "HELLO_Python_InDONESIA"
print(b.lower())

# Remove Whitespace
c = "Hello World on my Channel Python   "
print(c.strip())

# Replace String
d = "Hello, world!"
print(d.replace("e", "A"))

# Split String 
e = "Hello, World python Programming"
print(e.split(","))

#Replacing Sub Strings

s1 = 'The theory of data science is of the utmost importance.'
s2 = 'practice'

print('The new sentence: {}'.format(s1.replace('theory', s2)))