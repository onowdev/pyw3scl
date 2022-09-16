"""
Set
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.

* Note: Set items are unchangeable, but you can remove items and add new items.
Sets are written with curly brackets {}.
Set items are unordered, unchangeable, and do not allow duplicate values.
"""
print("Create Set")
tipedata_set = {"america","belanda","china"}
print(tipedata_set)

print("Get_length_of_a_set_TypeDate")
print(len(tipedata_set))

print("Set items can be of any data type:")
print("String, int and boolean data types:")
set_a = {"apple","banana","cherry"}
print(set_a)
print(type(set_a))
set_b = {1,7,9,3}
print(set_b)
print(type(set_b))
set_c = {True,False,True,False}
print(set_c)
print(type(set_c))