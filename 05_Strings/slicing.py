a = "Hello_Python"
print(a[2:7])

# Slice From the Start By leaving out the start index, the range will start at the first character:
print(a[:5])

# Slice To the End By leaving out the end index, the range will go to the end:

print(a[0:])

"""
Negative Indexing
Use negative indexes to start the slice from the end of the string:

Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
"""
print(a[-5:-2])

print(a[-4:-1])