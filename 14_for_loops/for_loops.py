"""
Python For Loops
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, 
and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

print("Looping Through A String")

for x in "Banana":
    print(x)

print("The Break Statement")
country = ["america","belanda","china","denmark","europe"]
for x in country:
    print(x)
    if x == "denmark":
        break