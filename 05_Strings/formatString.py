"""
String Format
As we learned in the Python Variables chapter, 
we cannot combine strings and numbers like this:
"""

age = 30
txt = "My name is Agus Sugiono, I am {}"

print(txt.format(age))
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity1 = 3
itemno1 = 567
price1 = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity1, itemno1, price1))