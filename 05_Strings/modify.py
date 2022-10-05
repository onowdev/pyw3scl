"""
Python - Modify Strings
Python has a set of built-in methods that you can use on strings.

"""

# Upper Case
a = "hello, world! my friend"
print(a.upper())

# LowerCase

b = "HELLO_Python_InDONESIA"
print(b.lower())

# Remove Whitespace
c = "Hello World on my Channel Python   "
print(c.strip())

# Replace String
d = "Hello, world!"
print(d.replace("e", "A"))

# Split String 
e = "Hello, World python Programming"
print(e.split(","))

#Replacing Sub Strings

s1 = 'The theory of data science is of the utmost importance.'
s2 = 'practice'

print('The new sentence: {}'.format(s1.replace('theory', s2)))

# Combining the Output of Multiple Lists
countries = ['USA', 'Canada', 'UK', 'Australia']
cities = ['Washington', 'Ottawa', 'London', 'Canberra']

for x, y in zip(countries, cities):
  print('The capital of {} is {}.'.format(x, y))

# Checking for Anagrams

from collections import Counter
def is_anagram(s1, s2):
  return Counter(s1) == Counter(s2)

s1 = 'listen'
s2 = 'silent'
s3 = 'runner'
s4 = 'neuron'

print('\'listen\' is an anagram of \'silent\' -> {}'.format(is_anagram(s1, s2)))
print('\'runner\' is an anagram of \'neuron\' -> {}'.format(is_anagram(s3, s4)))