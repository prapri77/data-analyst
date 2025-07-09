#types of operators in python
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Assignment Operators  
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Membership Operators
# 7. Identity Operators
# 8. Conditional Operators
# 9. Bitwise Shift Operators
# 10. Ternary Operator
# 11. Augmented Assignment Operators
# 12. Unary Operators
# 13. Floor Division Operator
# 14. Exponentiation Operator
# 15. Modulus Operator
# 16. String Operators
# 17. List Operators
# 18. Dictionary Operators
# 19. Set Operators
# 20. Lambda Operators

#this code demonstrates how to use different types of operators in Python.
# 1. Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# 2. Comparison Operators
print("\nComparison Operators:")
print("Equal:", a == b) 
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal To:", a >= b)
print("Less Than or Equal To:", a <= b)

# 3. Assignment Operators
print("\nAssignment Operators:")
x = 10
print("Initial value of x:", x)
x += 5 # Equivalent to x = x + 5
print("After += 5, x:", x)
x -= 3 # Equivalent to x = x - 3
print("After -= 3, x:", x)
x *= 2 # Equivalent to x = x * 2
print("After *= 2, x:", x)
x /= 4 # Equivalent to x = x / 4
print("After /= 4, x:", x)
x //= 2 # Equivalent to x = x // 2
print("After //= 2, x:", x)
x %= 3 # Equivalent to x = x % 3
print("After %= 3, x:", x)
x **= 2 # Equivalent to x = x ** 2
print("After **= 2, x:", x) 

# 4. Logical Operators
print("\nLogical Operators:")
a = True
b = False
print("AND:", a and b)
print("OR:", a or b)
print("NOT:", not a)

# 5. Bitwise Operators
print("\nBitwise Operators:")
x = 10 # 1010 in binary
y = 4 # 0100 in binary
print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT:", ~x)
print("Left Shift:", x << 2)
print("Right Shift:", x >> 2)

# 6. Membership Operators
print("\nMembership Operators:")
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)
print("Is 6 not in my_list?", 6 not in my_list) 

# 7. Identity Operators
print("\nIdentity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("Is x is y?", x is y)
print("Is x is not z?", x is not z)

# 8. Conditional Operators (Ternary Operator) syntax
# This operator allows you to assign a value based on a condition.
print("\nConditional Operators:")
a = 5
b = 10
max_value = a if a > b else b
print("Max value between a and b:", max_value)

# 9. Bitwise Shift Operators
print("\nBitwise Shift Operators:")
x = 8 # 1000 in binary
print("Left Shift (x << 2):", x << 2)   # Equivalent to 1000 << 2 = 1000000 (32 in decimal)
print("Right Shift (x >> 2):", x >> 2)  # Equivalent to 1000 >> 2 = 10 (2 in decimal)

# 10. Ternary Operator
print("\nTernary Operator:")
a = 5
b = 10
result = "a is greater" if a > b else "b is greater or equal"
print(result)

# 11. Augmented Assignment Operators
print("\nAugmented Assignment Operators:")
x = 10
print("Initial value of x:", x)
x += 5 # Equivalent to x = x + 5
print("After += 5, x:", x)
x -= 3 # Equivalent to x = x - 3
print("After -= 3, x:", x)
x *= 2 # Equivalent to x = x * 2
print("After *= 2, x:", x)
x /= 4 # Equivalent to x = x / 4
print("After /= 4, x:", x)
x //= 2 # Equivalent to x = x // 2
print("After //= 2, x:", x)
x %= 3 # Equivalent to x = x % 3
print("After %= 3, x:", x)
x **= 2 # Equivalent to x = x ** 2
print("After **= 2, x:", x) 

# 12. Unary Operators
print("\nUnary Operators:")
x = 5
print("Unary plus (+x):", +x)
print("Unary minus (-x):", -x) 

# 13. Floor Division Operator
print("\nFloor Division Operator:")
a = 10
b = 3
print("Floor Division (a // b):", a // b)  # Output: 3  

# 14. Exponentiation Operator
print("\nExponentiation Operator:")
base = 2
exponent = 3
print("Exponentiation (base ** exponent):", base ** exponent)  # Output: 8

# 15. Modulus Operator
print("\nModulus Operator:")
a = 10
b = 3
print("Modulus (a % b):", a % b)  # Output: 1

# 16. String Operators
print("\nString Operators:")
str1 = "Hello"
str2 = "World"
print("String Concatenation (str1 + str2):", str1 + " " + str2)
print("String Repetition (str1 * 3):", str1 * 3)  # Output: HelloHelloHello 

# 17. List Operators
print("\nList Operators:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List Concatenation (list1 + list2):", list1 + list2)
print("List Repetition (list1 * 2):", list1 * 2)  # Output: [1, 2, 3, 1, 2, 3]

# 18. Dictionary Operators
print("\nDictionary Operators:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print("Dictionary Concatenation (dict1 | dict2):", dict1 | dict2)  # Merging dictionaries in Python 3.9+
# Note: In earlier versions, you would use dict1.update(dict2) to merge dictionaries.

# 19. Set Operators
print("\nSet Operators:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Set Union (set1 | set2):", set1 | set2)
print("Set Intersection (set1 & set2):", set1 & set2)
print("Set Difference (set1 - set2):", set1 - set2)
print("Set Symmetric Difference (set1 ^ set2):", set1 ^ set2)

# 20. Lambda Operators
print("\nLambda Operators:")
add = lambda x, y: x + y
print("Lambda function result (add(5, 3)):", add(5, 3))  # Output: 8

# This code demonstrates how to use different types of operators in Python.
# It covers arithmetic, comparison, assignment, logical, bitwise, membership, identity, 
# conditional, bitwise shift, ternary, augmented assignment, unary, floor division, exponentiation, modulus, 
# string, list, dictionary, set operators and lambda functions.
