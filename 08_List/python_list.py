"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store 
collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets [ ] :
"""

print("Create List")

thisList = ["Apple", "Banana", "Cherry"]
print(thisList)

print("Access list items")
print(thisList[1])
print(thisList[0])

print("Change Value in list")
thisList[1] = "Blackcurrant"

print(thisList)