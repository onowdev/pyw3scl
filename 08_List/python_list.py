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
print("==============")
print("Change Value in list")

thisList[1] = "Blackcurrant"
print(thisList)

print("==============")
print("Loop with List")

thisList1 = ["Apple", "Banana", "Cherry", "Duku", "Edamame"]
for x in thisList1:
    print(x)

print("==============")
print("Check if in List")
thisList2 = ["apple","banana","cherry","duku"]
if "banana" in thisList2:
    print("Yes, 'apple' is in the fruits list")
print("==============")

print("Length in List")
thisList3 = ["apple","banana","cherry","duku"]
print(len(thisList3))
print("==============")

print("Add item in end of List")
thisList4 = ["apple","banana","cherry","duku"]
thisList4.append("EDAMAME")
print(thisList4)
print("==============")

print("Add item in specified list")
thisList5 = ["apple","banana","cherry","duku"]
thisList5.insert(1, "ORANGE")
print(thisList5)
print("==============")
print("Remove item in list")
print(thisList5)
thisList5.remove("duku")
print(thisList5)
print("==============")
print("Remove Last item in List")
print(thisList4)
thisList4.pop()
print(thisList4)
print("==============")
print("Remove specified item in list")
print(thisList3)
del thisList3[2]
print(thisList3)
print("Emty This List")
print(thisList2)
thisList2.clear()
print(thisList2)
print("===============")
print("Using Constructor to make list")

thisList6 = list(("America","Brunai","China","Denmark","Europe","Finland"))
print(thisList6)