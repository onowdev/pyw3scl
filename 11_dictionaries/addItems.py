from pprint import pprint
from turtle import pen


thisdict1 = {
    "brand" : "Bmw",
    "type" : "x5",
    "year" : 2022,
    "colour" : "silver"
}
print("before adding items")
print(thisdict1)
thisdict1["transmision"] = "AWD"
print("after add items")
print(thisdict1)