"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""

print("Hello_World!")
print("Hello_Agus_Sugiono")

# Assign String to a Variable Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings You can assign a multiline string to a variable by using three quotes:
b ="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(b)

"""
Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""

c = "Hello_World_Agus"
print(c[3])
print(c[7])

# Looping Through a String Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "Banana":
    print(x)
