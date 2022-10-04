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

# String Length To get the length of a string, use the len() function.

d = "Hello_world_In_Magelang"
print(len(d))

# Check String To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "practice make perfect"
print("perfect" in txt)

# Use it in an if statement:

txt2 = "The best things in life are Free!"
if "free" in txt2:
    print("Ya, 'free' is present.")

#string method

str1 = "FREECODECAMP IS COOL"
print(str1.lower())