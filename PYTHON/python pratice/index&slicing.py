# This code demonstrates how to use indexing and slicing in Python strings.
a = "python"
print(a[0])  # Output: 'p'
print(a[1:4])  # Output: 'yth'
print(a[-1])  # Output: 'n'
print(a[:-1])  # Output: 'pytho'
print(a[1:])  # Output: 'ython'
print(a[:3])  # Output: 'pyt'   
print(a[::2])  # Output: 'pto' (every second character)
print(a[::-1])  # Output: 'nohtyp' (reversed string)

b = [[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]]      
print(b[0][0])  # Output: 1 (first row, first column)
print(b[1][2])  # Output: 7 (second row, third column
print(b[2][1:3])  # Output: [10, 11] (third row, second and third columns)
print(b[1:3])  # Output: [[5, 6, 7, 8], [9, 10, 11, 12]] (second and third rows)
print(b[:2])  # Output: [[1, 2, 3, 4], [5, 6, 7, 8]] (first two rows)
print(b[::2])  # Output: [[1, 2, 3, 4], [9, 10, 11, 12]] (every second row)
print(b[::-1])  # Output: [[13, 14, 15, 16], [9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]] (reversed rows)
print(b[1][::-1])  # Output: [8, 7, 6, 5] (reversed second row)

# This code demonstrates how to use indexing and slicing .
c =  [[[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]],
      [ [ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12],
       [13, 14, 15, 16]]]
print(c[0][0][0])  # Output: 1 (first row, first column of the first sublist)
print(c[0][1][2])  # Output: 7 (second row, third column of the first sublist)
print(c[0][2][1:3])  # Output: [10, 11] (third row, second and third columns of the first sublist)
print(c[0][1:3])  # Output: [[5, 6, 7, 8], [9, 10, 11, 12]] (second and third rows of the first sublist)
print(c[0][:2])  # Output: [[1, 2, 3, 4], [5, 6, 7, 8]] (first two rows of the first sublist)
print(c[0][::2])  # Output: [[1, 2, 3, 4], [9, 10, 11, 12]] (every second row of the first sublist)
print(c[0][::-1])  # Output: [[13, 14, 15, 16], [9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]] (reversed rows of the first sublist)
print(c[0][1][::-1])  # Output: [8, 7, 6, 5] (reversed second row of the first sublist)


# This code demonstrates how to use indexing and slicing in Python tuples.
d = (1, 2, 3, 4)
print(d[0])  # Output: 1
print(d[1:3])  # Output: (2, 3)
print(d[-1])  # Output: 4
print(d[:-1])  # Output: (1, 2, 3)
print(d[1:])  # Output: (2, 3, 4)
print(d[:3])  # Output: (1, 2, 3)
print(d[::2])  # Output: (1, 3)
print(d[::-1])  # Output: (4, 3, 2, 1)

# This code demonstrates how to use indexing and slicing in Python lists.
e = [1, 2, 3, 4]
print(e[0])  # Output: 1
print(e[1:3])  # Output: [2, 3]
print(e[-1])  # Output: 4
print(e[:-1])  # Output: [1, 2, 3]
print(e[1:])  # Output: [2, 3, 4]
print(e[:3])  # Output: [1, 2, 3]
print(e[::2])  # Output: [1, 3]
print(e[::-1])  # Output: [4, 3, 2, 1]

# This code demonstrates how to use indexing and slicing in Python dictionaries.
f = { "a": 1, "b": 2, "c": 3, "d": 4 }
# Note: Dictionaries do not support indexing or slicing like lists or tuples.
# However, you can access values using keys.
print(f["a"])  # Output: 1
print(f["b"])  # Output: 2
print(f["c"])  # Output: 3
print(f["d"])  # Output: 4
print(list(f.keys())[0])  # Output: 'a' (first key)
print(list(f.values())[0])  # Output: 1 (first value)
print(list(f.items())[0])  # Output: ('a', 1) (first key-value pair)
print(list(f.keys())[1:3])  # Output: ['b', 'c'] (second and third keys)

my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "New York"  # Adds a new key-value pair
my_dict["age"] = 31          # Updates the value for an existing key
print(my_dict)

# This code demonstrates how to use indexing and slicing in Python sets.
g = {1, 2, 3, 4}
print(1 in g)  # Output: True (check if 1 is in the set)
print(5 in g)  # Output: False (check if 5 is in the set)
print(len(g))  # Output: 4 (number of elements in the set) 
# Note: Sets do not support indexing or slicing like lists or tuples.

a = eval(input("> "))
b = eval(input("> "))
print(a+b) # Concatenates the two input strings to avoid we use eval to evaluate the input as a Python expression.
print(a-b) # Subtracts the second input from the first input.

print("student name mark grade dynamical using input")

# This code demonstrates how to take dynamic input for student names, marks, and grades.
name = eval(input("Enter the name of students: "))
marks = eval(input("Enter the marks of students: "))
grade = eval(input("Enter the grade of students: "))

# prints the student name, marks, and grade using f-string formatting
print(f"Student Name: {name}, Marks: {(marks/1200)*100}, Grade: {grade/10}") 

# prints the student name, marks, and grade using str.format()
print("Student Name: {}, Marks: {}, Grade: {}".format(name, marks, grade)) 

# prints the student name, marks, and grade using old-style string formatting
print("student %s name mark %d grade %.2f dynamical using input" % (name, marks, grade)) 

