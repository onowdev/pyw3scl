"""
Python For Loops
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, 
and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

print("Looping Through A String")

for x in "Banana":
    print(x)

print("The Break Statement")
country = ["america","belanda","china","denmark","europe"]
for x in country:
    print(x)
    if x == "denmark":
        break

print("The continue Statement")

Angka = [1,2,3,4,5,6,7,8,9]
for x in Angka:
    if x == 3:
        continue
    print(x)
print("Range Function")

for x in range(9):
    print(x)

print("Range Function V2")
for x in range (3,9):
    print(x)

print("Range in Loops dengan kelipatan berbatas")
for x in range(2, 30, 5):
    print(x)

print("Else in For Loop")
for x in range(9):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finnally finished")