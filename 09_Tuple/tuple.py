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
print("===============")
print("check item in tupple")
print(thistuple)
if "apple" in thistuple:
    print("Yes 'apple' is in the fruit tuple")

print("Tuple Length")
print(thistuple)
print(len(thistuple))

print("Del a Tuple")
thistuple2 = ("america","Belgium","China","Denmark","Europe")
print(thistuple2)
del thistuple2
# print(thistuple2)

# Using Constructor for Tuple
print("Using Constructor for Tuple")
thistuple3 = tuple(("apple","banana","cherry","duku"))
print(thistuple3)

#Combile Tuple

tupleOne = ("one", "two")
tupleTwo = ("three", "four")
tupleThree = tupleOne + tupleTwo
print(tupleThree) # ("one", "two", "three", "four")

#Sorting Tuple

myTuple =  ("a", "c", "e", "b", "f", "d", "g", "z", "w", "x")
myNumberTuple = (1, 3, 5, 2, 7, 4, 6)

newTuple = sorted(myTuple)
newNumberTuple = sorted(myNumberTuple)

print(newTuple) # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'w', 'x', 'z')
print(newNumberTuple) # (1, 2, 3, 4, 5, 6, 7)