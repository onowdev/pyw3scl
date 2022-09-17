"""
Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, 
changeable and do not allow duplicates.
Dictionaries are written with curly brackets, and have keys and values: {}
"""

print("Create Dictionary")
thisdict = {
    "brand" : "BMW",
    "model" : "X5",
    "year"  : " 2022"
}
print(thisdict)
print(thisdict["model"])

# Changeable Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Duplicates Not Allowed Dictionaries cannot have two items with the same key:
thisdict = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : "2022",
    "year" : "1962"
}
print(thisdict)

print("Dictionary Length")

print(len(thisdict))