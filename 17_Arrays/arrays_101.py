# Arrays are used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]

print(cars)

#accesing array
print(cars[0])

#length arrray

print(len(cars))

#looping array

for x in cars:
    print(x)

# adding arrays element

cars.append("Honda")
print(cars)

# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
	print (a[i], end =" ")
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
	print (b[i], end =" ")
