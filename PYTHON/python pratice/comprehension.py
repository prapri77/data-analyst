# Comprehension in Python

# Comprehension is a concise way to create sequences like lists, sets, or dictionaries.
# It allows you to generate new sequences by applying an expression to each item in an iterable.

#syntax = [expression or true, conditions, filters]
# List comprehension example:
squares = [x**2 for x in range(10) if x%2 ==0]
print(squares)  # Output: [0, 4, 16, 36, 64]

# Set comprehension example:
unique_lengths = {len(word) for word in ["apple", "banana", "cherry"]}
print(unique_lengths)  # Output: {5, 6}

# Dictionary comprehension example:
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Tuple comprehension example (using generator expression):
squared_gen = (x**2 for x in range(5))
print(tuple(squared_gen))  # Output: (0, 1, 4, 9, 16)

l1 = [1,2,3,3,4,5,6]
l3 = {i*2 for i in l1}
print(l3)

l2 = [i*2 for i in l1]
print(l2)  # Output: [2, 4, 6, 8, 10, 12]

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)] #first i=1 then j=1,2,3
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

l_3d = [[[j * k for k in range(1, 4)] for j in range(1, 4)] for i in range(1, 4)] #first i=1 then j=1,2,3
print("3d:",l_3d)
l4 = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

flattened_tuple = tuple(element for row in l4 for element in row)
print(flattened_tuple)

d1 = {e:e*e for e in range(7)}
print(d1)