# python variables topics
# print("python")
print("Large language models")

_kiwi = "kiwi"
print(_kiwi)

Grapes = 34
#print(grapes) here would raise an error because variable names are case-sensitive

# when we create a data type in python it will stored in one time

a = 33
b = 33
print(id(a))
print(id(b))

# 1. Variable Assignment
x = 5
y = "Hello, World!"

# 2. Variable Types
a = 10          # Integer
b = 3.14       # Float
c = True       # Boolean
d = "Python"   # String
e = [1, 2, 3]  # List
f = (4, 5, 6)  # Tuple
g = { "key": "value" }  # Dictionary
h = {1, 2, 3}  # Set
# 2.1 Type Conversion
int_var = int(3.14)  # Converts float to integer
float_var = float(10)  # Converts integer to float
str_var = str(100)  # Converts integer to string
# 2.2 Type Checking
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>

# 3. Dynamic Typing
x = 5
x = "Now I'm a string"

# 4. Constants
PI = 3.14159

# 5. Variable Scope
def my_function():
    local_var = "I'm local"
    print(local_var)    

my_function()
# print(local_var)  # This would raise an error because local_var is not defined outside

# 6. Global Variables
global_var = "I'm global"

def access_global_var():
    print(global_var)

access_global_var()


# 7. Variable Naming Conventions
my_variable = 1          # snake_case
MyVariable = 2           # PascalCase
myVariable = 3           # camelCase    
# 8. Multiple Assignment
a, b, c = 1, 2, 3   
# 9. Swapping Variables
x, y = y, x

# 10. Type Hinting
def add_numbers(a: int, b: int) -> int:
    return a + b
print(add_numbers(5, 10))  # Output: 15 

# 11. Type Checking how to print var
var= 42
def check_type(var):
    if isinstance(var, int):
        return "It's an integer"
    elif isinstance(var, str):
        return "It's a string"
    else:
        return "Unknown type" 
print(check_type(var))  # Output: It's an integer

# 12. Variable Annotations
def greet(name: str) -> str:
    return f"Hello, {name}!" 
print(greet("Alice"))  # Output: Hello, Alice!

# 13. Mutable vs Immutable Types
# Mutable: Lists, Dictionaries, Sets
# Immutable: Tuples, Strings, Frozensets

# Example of mutable type
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]  

# Example of a dictionary
my_dict = {"key": "value"}  
my_dict["new_key"] = "new_value"
print(my_dict)  # Output: {'key': 'value', 'new_key': 'new_value'}

# Example of a set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Example of a string (immutable)
my_string = "Hello"
# my_string[0] = "h"  # This would raise an error because strings are immutable

# Example of immutable type
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise an error because tuples are immutable

# Example of a frozenset
my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4)  # This would raise an error because frozensets are immutable

# 14. Variable Length Arguments
def variable_length_args(*args):
    for arg in args:
        print(arg)
variable_length_args(1, 2, 3, "Hello", [4, 5])

# 15. Keyword Arguments
def keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

keyword_arguments(name="Alice", age=30, city="New York")
# 16. Boolean Variables
print(type(True))

a ="hello" 
print(type(a))
print(bool(a))  # Output: True, because non-empty strings are truthy
print(repr(a))  # Output: "'hello'", gives a string representation of 'a'
print(ascii(a))  # Output: "'hello'", gives an ASCII representation of 'a'
print(id(a))  # Output: Memory address of 'a'
print(str(a))  # Output: 'hello', converting string to string (no change)

# The following conversions will raise errors because 'a' is a string, not a number
#print(int(a))  # This will raise an error because 'a' is a string, not an integer
#print(float(a))  # This will raise an error because 'a' is a string, not a float

#print(complex(a))  # This will raise an error because 'a' is a string, not a number
#print(bin(a))  # This will raise an error because 'a' is a string, not a number
# print(hex(a))  # This will raise an error because 'a' is a string, not a number
# print(oct(a))  # This will raise an error because 'a' is a string, not a number


b = True
print(type(b))  # Output: <class 'bool'>
print(bool(b))  # Output: True, because 'b' is already a boolean
print(int(b))  # Output: 1, True is converted to 1  
print(float(b))  # Output: 1.0, True is converted to 1.0
print(str(b))  # Output: 'True', converting boolean to string
print(complex(b))  # Output: (1+0j), True is converted to complex number
print(bin(b))  # Output: '0b1', binary representation of True
print(hex(b))  # Output: '0x1', hexadecimal representation of True
print(oct(b))  # Output: '0o1', octal representation of True
print(repr(b))  # Output: 'True', gives a string representation of 'b'
print(ascii(b))  # Output: 'True', gives an ASCII representation of 'b

c = 8.0
print(type(c))  # Output: <class 'float'>
print(bool(c))  # Output: True, because non-zero floats are truthy
print(int(c))  # Output: 8, converting float to int (truncating)
print(float(c))  # Output: 8.0, converting float to float (no change)
print(str(c))  # Output: '8.0', converting float to string
print(complex(c))  # Output: (8+0j), converting float to complex number
print(repr(c))  # Output: '8.0', gives a string representation of 'c'
print(ascii(c))  # Output: '8.0', gives an ASCII representation of 'c'

# The following conversions will raise errors because 'c' is a float, not an integer
# print(bin(c))  # This will raise an error because 'c' is a float, not an integer
# print(hex(c))  # This will raise an error because 'c' is a float, not an integer
# print(oct(c))  # This will raise an error because 'c' is a float, not an integer

d = 42 + 0j
print(type(d))  # Output: <class 'complex'>
print(bool(d))  # Output: True, because non-zero complex numbers are truthy
print(str(d))  # Output: '(42+0j)', converting complex to string
print(complex(d))  # Output: (42+0j), converting complex to complex (no change)
print(repr(d))  # Output: '(42+0j)', gives a string representation of 'd'
print(ascii(d))  # Output: '(42+0j)', gives an ASCII representation of 'd'

# The following conversions will raise errors because 'd' is a complex number, not a float
# print(bin(d))  # This will raise an error because 'd' is a complex number, not an integer
# print(hex(d))  # This will raise an error because 'd' is a complex number, not an integer
# print(oct(d))  # This will raise an error because 'd' is a complex number, not an integer
# print(int(d))  # This will raise an error because 'd' is a complex number, not an integer
# print(float(d))  # This will raise an error because 'd' is a complex number, not a float

e = None
print(type(e))  # Output: <class 'NoneType'>
print(bool(e))  # Output: False, because None is falsy
print(str(e))  # Output: 'None', converting None to string
print(repr(e))  # Output: 'None', gives a string representation of 'e'
print(ascii(e))  # Output: 'None', gives an ASCII representation of 'e'

# The following conversions will raise errors because 'e' is None, not a number
# print(int(e))  # This will raise an error because 'e' is None, not an integer
# print(float(e))  # This will raise an error because 'e' is None, not a float
# print(complex(e))  # This will raise an error because 'e' is None, not a number
# print(bin(e))  # This will raise an error because 'e' is None, not an integer
# print(hex(e))  # This will raise an error because 'e' is None, not an integer
# print(oct(e))  # This will raise an error because 'e' is None, not an integer

h = 0b1010  # Binary representation of 10
print(type(h))  # Output: <class 'int'>
print(bool(h))  # Output: True, because non-zero integers are truthy
print(int(h))  # Output: 10, converting binary to integer (no change)   
print(float(h))  # Output: 10.0, converting binary to float
print(str(h))  # Output: '10', converting binary to string
print(complex(h))  # Output: (10+0j), converting binary to complex
print(repr(h))  # Output: '10', gives a string representation of 'h'
print(ascii(h))  # Output: '10', gives an ASCII representation of 'h'

j = 0x1A  # Hexadecimal representation of 26
print(type(j))  # Output: <class 'int'>
print(bool(j))  # Output: True, because non-zero integers are truthy
print(int(j))  # Output: 26, converting hexadecimal to integer (no change)
print(float(j))  # Output: 26.0, converting hexadecimal to float
print(str(j))  # Output: '26', converting hexadecimal to string
print(complex(j))  # Output: (26+0j), converting hexadecimal to complex
print(repr(j))  # Output: '26', gives a string representation of 'j'
print(ascii(j))  # Output: '26', gives an ASCII representation of 'j'

k = 0o32  # Octal representation of 26
print(type(k))  # Output: <class 'int'>
print(bool(k))  # Output: True, because non-zero integers are truthy
print(int(k))  # Output: 26, converting octal to integer (no change)
print(float(k))  # Output: 26.0, converting octal to float
print(str(k))  # Output: '26', converting octal to string
print(complex(k))  # Output: (26+0j), converting octal to complex
print(repr(k))  # Output: '26', gives a string representation of 'k'
print(ascii(k))  # Output: '26', gives an ASCII representation of 'k'
