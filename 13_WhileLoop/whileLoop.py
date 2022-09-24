"""
Python Loops
Python has two primitive loop commands:

1. while loops
2. for loops

"""

print("While Loops")
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

a = 7
while a < 7:
    print(a)
    a +=7

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
print("The Break statement")
i = 1
while i < 6:
    print(i)
    if (1 == 3):
        break
    i += 1