"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets ().
"""
#Create Tuple
myTuple = ("apple","banana","cherry")

print(myTuple)

#Access Tuple
myTuple1 =("america","bahama","cuba","dominico","Euro")
print(myTuple1[3])

#Change Value of Tuple
print(myTuple1)
# myTuple1[0] = "Armenia"

# print(myTuple1) #output Error
# Unchangeable : Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

#Loop tuple
thistuple = ("apple","banana","cherry","duku")
for x in thistuple:
    print(x)