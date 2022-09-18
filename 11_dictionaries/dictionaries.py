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

print("Dictionary Items - Data Types The values in dictionary items can be of any data type:")

thisdict1 = {
    "brand" : "Mobil SMK",
    "electric" : True,
    "year" : 1965,
    "colors" : ["red", "white", "blue"]
}
print("thisdict1 :",thisdict1)
print("the type data of 'thisdict1' ", type(thisdict1))

print("Print All value one by one in dictionary data type")

thisdict2 = {
    "brand" : "toyota",
    "year" : "2022",
    "model" : "landcruiser"
}
for x in thisdict2:
    print(thisdict2[x])

print("using value Function to return value in dictionary")

thisdict3 = {
    "brand" : "toyota",
    "year" : "2022",
    "model" : "lexus"
}
for x in thisdict3.values():
    print(x)