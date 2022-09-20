"""
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
"""
print("Create a dictionary that contain three dictionaries:")

myChild = {
    "child1" : {
        "name" : "Andra",
        "sex" : "male",
        "year" : "2016"
    },
    "child2" : {
        "name" : "chandra",
        "sex" : "male",
        "year" : "2024"
    },
    "child3" : {
        "name" : "Felicia",
        "sex" : "female",
        "year" : "2027"
    }
}

print(myChild)

print("Create three dictionaries, then create one dictionary that will contain the other three dictionaries:")

child1 = {
    "name" : "andra",
    "year" : 2016
}
child2 = {
    "name" : "chandra",
    "year" : "2024"
}
child3 = {
    "name" : "Felicia",
    "year" : "2027"
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)