"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are 
the keys of the dictionary, but there are methods to return the values as well
"""
print("loop in dictionary")
thisdict1 = {
    "nama" : "Agus",
    "usia" : "30",
    "status" : "bapak anak 1"
}
print(thisdict1)

for x in thisdict1:
    print(x)

print("Print all values in the dictionary, one by one:")

for x in thisdict1:
    print(thisdict1[x])
print("You can also use the values() method to return values of a dictionary:")

for x in thisdict1.values():
    print(x)

print("You can use the keys() method to return the keys of a dictionary:")

for x in thisdict1.keys():
    print(x)

print("Loop through both keys and values, by using the items() method:")

for x,y in thisdict1.items():
    print(x,y)