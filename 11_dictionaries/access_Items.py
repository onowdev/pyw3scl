"""
Accessing Items
You can access the items of a dictionary 
by referring to its key name, inside square brackets:
"""
print("Accessing Items")
thisdict = {
    "brand" : "Toyota",
    "model" : "All New Land Cruiser",
    "year" : "2022"
}
x = thisdict["model"]
print(thisdict)
print("the car is" , x)

"""
Get Keys
The keys() method will return a list of all the keys in the dictionary.

"""
a = thisdict.keys()
print(a)

print("====================")
print("Add a new item to the original dictionary")
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1960
}
b = car.keys()
print(a) # before the Change

car ["color"] = "Black"

print(b) #After the Change