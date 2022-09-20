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
