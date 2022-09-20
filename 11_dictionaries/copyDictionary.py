"""
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""
thisdict = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1965
}
print("Make a copy of a dictionary with the copy() method:")
mydict = thisdict.copy()
print(mydict)

print("Make a copy of a dictionary with the dict() function:")

mydict1 = dict(thisdict)
print(mydict1)