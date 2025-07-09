# Example: Accessing elements of a list using a for loop

my_list = [10, 20, 30, 40, 50]

for item in my_list:
    print(item)

# Using break in a for loop
for item in my_list:
    if item == 30:
        break
    print("Break example:", item)

# Using continue in a for loop
for item in my_list:
    if item == 30:
        continue
    print("Continue example:", item)

else:
    print("end of the loop")

# 2-dimensional array
l_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in l_2d:
    print(row)
    print()
    for element in row:
        print(element)
print("$$$$end of the loop$$$$")
# 3-dimensional array 
l_3d = [
    [
        [1, 2], 
        [3, 4]
    ],
    [
        [5, 6], 
        [7, 8]
    ]
]
for row in l_3d:
    print(row) #[i]
    print()
    for row1 in row:
        print(row1) #[i][j]
        for element in row1:
            print(element) #[i][j][k]
else:
    print("end of the loop")

# zip: The zip() function combines multiple iterables (like lists or tuples) element-wise into tuples.
# Syntax: zip(iterable1, iterable2, ...)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
l3 = dict(zip(list1,list2))
print(l3)

# Using zip in a loop
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")