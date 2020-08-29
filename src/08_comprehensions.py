"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [item+1 for item in range(5)]
print(y)

z = list(map(lambda z: z+1, range(5)))
print(z)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [item**3 for item in range(10)]
print(y)

x = list(map(lambda x: x**3, range(10)))
print(x)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]
print(y)

x = list(map(lambda word: word.upper(), a))
print(x)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

y = [int(even) for even in x if int(even) % 2 == 0]
print(y)

z = list(filter(lambda even: int(even) % 2 == 0, x))
print(z)
