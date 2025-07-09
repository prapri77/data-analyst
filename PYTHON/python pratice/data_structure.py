#types of data structures in Python

# This code demonstrates how to use different types of data structures in Python.

print("***********list***********")
# 1. List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

#list is a collection which is ordered and changeable. Allows duplicate members.
# Lists are defined by having values between square brackets [].
# Lists can contain elements of different data types, including other lists.
# Lists are mutable, meaning you can change their content after creation.
# Lists support various operations like appending, removing, and slicing elements.
# Lists can be nested, meaning you can have lists within lists.
# Lists are commonly used for storing collections of items, such as numbers, strings, or objects.
# Lists can be iterated over using loops, allowing you to access each element in sequence.
#example of list operations:
my_list.append(6)  # Adding an element
my_list.remove(2)  # Removing an element
print("Updated List:", my_list)
# Lists can be sorted using the sort() method or the sorted() function.
# Lists can be sliced to access a subset of elements, e.g., my_list[1:3] gives elements at index 1 and 2.
# Lists can be concatenated using the + operator, e.g., my_list + [7, 8] combines two lists.
# Lists can be repeated using the * operator, e.g., my_list * 2 creates a new list with elements repeated.
# Lists can be checked for membership using the in operator, e.g., 3 in my_list returns True if 3 is present.
# Lists can be used to store heterogeneous data, meaning they can contain different data types in the same list.   
#example of heterogeneous list:
heterogeneous_list = [1, "two", 3.0, [4, 5], {'six': 6}]
# Heterogeneous lists can be useful for storing related but different types of data together.
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List:", heterogeneous_list)
# Heterogeneous lists can be useful for storing related but different types of data together.
# Example of accessing elements in a heterogeneous list:
print("First element:", heterogeneous_list[0])  # Accessing the first element
print("Second element:", heterogeneous_list[1])  # Accessing the second element
# Example of accessing elements in a heterogeneous list:
print("Nested list element:", heterogeneous_list[3][1])  # Accessing an element
# from the nested list
# Example of accessing elements in a heterogeneous list:
print("Dictionary element:", heterogeneous_list[4]['six'])  # Accessing a value from
# the dictionary in the list
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Length:", len(heterogeneous_list))  # Getting the length  of the heterogeneous list
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Type:", type(heterogeneous_list))  # Getting the type of the heterogeneous list
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Elements:", heterogeneous_list)  # Printing the entire heterogeneous list
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Elements:", [type(item) for item in heterogeneous_list])  # Getting the types of each element in the heterogeneous list
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Elements:", [str(item) for item in heterogeneous_list])
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Elements:", [repr(item) for item in heterogeneous_list])
# Example of accessing elements in a heterogeneous list:
print("Heterogeneous List Elements:", [item for item in heterogeneous_list if isinstance(item, int)])  # Filtering only integer elements from the heterogeneous list

#list with operators
# Lists can be manipulated using various operators and methods.
# Concatenation: Combining two lists using the + operator

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print("Combined List:", combined_list)

# Repetition: Repeating a list using the * operator
repeated_list = list1 * 2
print("Repeated List:", repeated_list)

# Membership: Checking if an element is in a list using the in operator
is_in_list = 2 in list1
print("Is 2 in list1?", is_in_list)

# Length: Getting the number of elements in a list using the len() function
list_length = len(list1)
print("Length of list1:", list_length)

# Indexing: Accessing elements in a list using their index

# Accessing the first element
first_element = list1[0]
print("First element of list1:", first_element)

# Slicing: Getting a subset of elements from a list using slicing syntax

sliced_list = list1[1:3]  # Getting elements from index 1
# to index 2 (exclusive)
print("Sliced List (index 1 to 2):", sliced_list)

# Sorting: Sorting a list using the sort() method

unsorted_list = [3, 1, 4, 2]
unsorted_list.sort()  # Sorting the list in ascending order
print("Sorted List:", unsorted_list)

# Reversing: Reversing the order of elements in a list using the reverse() method

unsorted_list.reverse()  # Reversing the list
print("Reversed List:", unsorted_list)

# Appending: Adding an element to the end of a list using the append() method

list1.append(4)  # Adding 4 to the end of list1
print("List1 after appending 4:", list1)

# Inserting: Adding an element at a specific index in a list using the insert() method

list1.insert(1, 10)  # Inserting 10 at index 1
print("List1 after inserting 10 at index 1:", list1)

# Removing: Removing an element from a list using the remove() method

list1.remove(10)  # Removing 10 from list1
print("List1 after removing 10:", list1)

list1.extend(unsorted_list)  # Adding multiple elements to list1
print("List1 after extending with [5, 6]:", list1)

# Popping: Removing and returning the last element of a list using the pop() method

popped_element = list1.pop()  # Removing the last element
print("Popped Element from List1:", popped_element)
print("List1 after popping the last element:", list1)

print("***********tuple***********")
# 2. Tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are defined by having values between parentheses ().
# Tuples are immutable, meaning you cannot change their content after creation.
# Tuples can contain elements of different data types, including other tuples.
# Tuples support various operations like indexing, slicing, and concatenation.
# Tuples can be nested, meaning you can have tuples within tuples.
# Tuples are commonly used for storing fixed collections of items, such as coordinates or RGB values.
# Tuples can be iterated over using loops, allowing you to access each element in sequence

# Example of tuple operations:
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)
# Tuples are immutable, so we cannot change their content directly.

# However, we can create a new tuple with modified content.
new_tuple = my_tuple + (6,)  # Adding an element by concatenation
print("New Tuple after adding 6:", new_tuple)

# Tuples can be sliced to access a subset of elements, e.g., my_tuple[1:3] gives elements at index 1 and 2.
sliced_tuple = my_tuple[1:3]
print("Sliced Tuple (index 1 to 2):", sliced_tuple)

# Tuples can be concatenated using the + operator, e.g., my_tuple + (6, 7) combines two tuples.
concatenated_tuple = my_tuple + (6, 7)
print("Concatenated Tuple:", concatenated_tuple)

# Tuples can be repeated using the * operator, e.g., my_tuple * 2 creates a new tuple with elements repeated.
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)

# Tuples can be checked for membership using the in operator, e.g., 3 in my_tuple returns True if 3 is present.
is_in_tuple = 3 in my_tuple
print("Is 3 in my_tuple?", is_in_tuple)
# Tuples can be used to store heterogeneous data, meaning they can contain different data types in the same tuple.

# Example of heterogeneous tuple:
heterogeneous_tuple = (1, "two", 3.0, (4, 5), {'six': 6})
print("Heterogeneous Tuple:", heterogeneous_tuple)
# Heterogeneous tuples can be useful for storing related but different types of data together.
# Example of accessing elements in a heterogeneous tuple:
print("First element:", heterogeneous_tuple[0])  # Accessing the first element
print("Second element:", heterogeneous_tuple[1])  # Accessing the second element
# Example of accessing elements in a heterogeneous tuple:
print("Nested tuple element:", heterogeneous_tuple[3][1])  # Accessing an element

# from the nested tuple
# Example of accessing elements in a heterogeneous tuple:
print("Dictionary element:", heterogeneous_tuple[4]['six'])  # Accessing a value from


print("Heterogeneous Tuple Length:", len(heterogeneous_tuple))  # Getting the length of the heterogeneous tuple
print("Heterogeneous Tuple Type:", type(heterogeneous_tuple))  # Getting the type of the heterogeneous tuple
print("Heterogeneous Tuple Elements:", heterogeneous_tuple)  # Printing the entire heterogeneous tuple
print("Heterogeneous Tuple Elements:", [type(item) for item in heterogeneous_tuple])  # Getting the types of each element in the heterogeneous tuple
print("Heterogeneous Tuple Elements:", [str(item) for item in heterogeneous_tuple]) 
print("Heterogeneous Tuple Elements:", [repr(item) for item in heterogeneous_tuple])  # Getting the string representation of each element in the heterogeneous tuple
print("Heterogeneous Tuple Elements:", [item for item in heterogeneous_tuple if isinstance(item, int)])  # Filtering only integer elements from the heterogeneous tuple
# Example of accessing elements in a heterogeneous tuple:
print("Heterogeneous Tuple Elements:", [item for item in heterogeneous_tuple if isinstance(item, str)])  # Filtering only string elements from the heterogeneous tuple


# 3. Set
print("***********set***********")
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
# set is a collection which is unordered, unindexed, and does not allow duplicate members.
# Sets are defined by values between curly braces {}.
# Sets are mutable, meaning you can add or remove elements after creation.
# Sets are commonly used for membership testing, removing duplicates, and mathematical set operations.

# Example of set operations:
my_set.add(6)  # Adding an element
my_set.discard(2)  # Removing an element if present
print("Updated Set:", my_set)

# Sets do not support indexing or slicing because they are unordered.
# Sets can be iterated over using loops.
for item in my_set:
    print("Set item:", item)

# Set operations: union, intersection, difference, symmetric difference
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# issubset and issuperset examples
set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5, 6}


# Check if set_x is a subset of set_y
print("Is set_x a subset of set_y?", set_x.issubset(set_y))  # True

# Check if set_y is a superset of set_x
print("Is set_y a superset of set_x?", set_y.issuperset(set_x))  # True

# Check if set_x is a superset of set_y
print("Is set_x a superset of set_y?", set_x.issuperset(set_y))  # False

# Check if set_y is a subset of set_x
print("Is set_y a subset of set_x?", set_y.issubset(set_x))  # False

# Sets can be used to remove duplicates from a list
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print("Unique elements from list:", unique_set)

# Creating 10 different set variables
set1 = {1, 2, 3}


# Demonstrating add, remove, pop, discard, on set1
set1.add(100)
print("set1 after add(100):", set1)
set1.remove(2)
print("set1 after remove(2):", set1)
popped = set1.pop()
print("set1 after pop():", set1, "| Popped element:", popped)
set1.discard(200)  # 200 not in set, so nothing happens
print("set1 after discard(200):", set1)


# isdisjoint: Returns True if two sets have no elements in common
set2 = {7, 8, 9}
set3 = {3, 4, 5}
print("Is set1 disjoint with set2?", set1.isdisjoint(set2))  # True, no common elements
print("Is set1 disjoint with set3?", set1.isdisjoint(set3))  # False, common element(s) exist
set2.update(set3)
print("updated set2",set2)


# 4. Dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)
#dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionaries are defined by having key-value pairs enclosed in curly braces {}.
# Dictionaries are mutable, meaning you can change their content after creation.
# Dictionaries store data in key-value pairs, where each key is unique.
# Dictionaries support various operations like adding, removing, and accessing elements by key.
# Dictionaries can be nested, meaning you can have dictionaries within dictionaries.
# Dictionaries are commonly used for storing structured data, such as configuration settings or user profiles.

# Example of dictionary operations:
print("***********dictionary***********")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)

my_dict.get('a')  # Accessing a value by its key
print("Value for key 'a':", my_dict.get('a'))

my_dict['b'] = 20  # Modifying a value by its key
print("Dictionary after modifying 'b':", my_dict)

my_dict['c'] += 5  # Incrementing a value by its key
print("Dictionary after incrementing 'c':", my_dict)

# Adding a new key-value pair
my_dict['d'] = 4
print("Dictionary after adding 'd':", my_dict)

d2 ={'e': 5, 'f': 6}
my_dict.update(d2)  # Merging another dictionary
print("Dictionary after merging with d2:", my_dict)

# Removing a key-value pair
my_dict.pop('b')
print("Dictionary after removing 'b':", my_dict)

my_dict.pop('c', None)  # Removing a key safely, returns None if key doesn't exist
print("Dictionary after safely removing 'c':", my_dict)

del my_dict['d']  # Deleting a key-value pair
print("Dictionary after deleting 'a':", my_dict)

my_dict.popitem()  # Removing and returning the last inserted key-value pair
print("Dictionary after popping the last item:", my_dict)

# Accessing a value by its key
value_a = my_dict['a']
print("Value for key 'a':", value_a)

# Checking if a key exists in the dictionary
key_exists = 'c' in my_dict
print("Does key 'c' exist in the dictionary?", key_exists)

# Dictionaries can be iterated over using loops, allowing you to access each key-value pair in sequence.
print("Iterating over dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Dictionaries can be sorted by keys or values using the sorted() function.
sorted_dict_by_keys = dict(sorted(my_dict.items()))
print("Dictionary sorted by keys:", sorted_dict_by_keys)

# Dictionaries can be sorted by values using the sorted() function with a custom key.
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1])) 
print("Dictionary sorted by values:", sorted_dict_by_values)
# Example of accessing elements in a dictionary:
print("Keys in my_dict:", my_dict.keys())  # Getting all keys
print("Values in my_dict:", my_dict.values())  # Getting all values
print("Items in my_dict:", my_dict.items())  # Getting all key-value pairs  

# Example of accessing elements in a dictionary:
print("First key in my_dict:", list(my_dict.keys())[0])  # Accessing the first key
print("First value in my_dict:", list(my_dict.values())[0])  # Accessing the first value
print("First item in my_dict:", list(my_dict.items())[0])  # Accessing the first key-value pair
# Example of accessing elements in a dictionary:
print("Dictionary Length:", len(my_dict))  # Getting the length of the dictionary
# Example of accessing elements in a dictionary:
print("Dictionary Type:", type(my_dict))  # Getting the type of the dictionary
# Example of accessing elements in a dictionary:
print("Dictionary Elements:", my_dict)  # Printing the entire dictionary
# Example of accessing elements in a dictionary:
print("Dictionary Elements:", [type(item) for item in my_dict.items()])  #
# Getting the types of each key-value pair in the dictionary
print("Dictionary Elements:", [str(item) for item in my_dict.items()])
# Getting the string representation of each key-value pair in the dictionary
print("Dictionary Elements:", [repr(item) for item in my_dict.items()])  #
# Getting the string representation of each key-value pair in the dictionary
print("Dictionary Elements:", [item for item in my_dict.items() if isinstance(item[1], int)])  # Filtering only integer values from the dictionary
# Example of accessing elements in a dictionary:
print("Dictionary Elements:", [item for item in my_dict.items() if isinstance(item[1], str)])  # Filtering only string values from the dictionary

#list values
l3= [1, 2, 3]
# dict(l3)  # Converting a list to a dictionary with keys as indices and values as elements
# Convert list to dictionary
l3 = dict.fromkeys(l3, 25)  # Creating a dictionary with keys from the list and default value 25
print("Dictionary from list with default value:", l3)
my_dict_from_list = {i: value for i, value in enumerate(l3)}
print("Dictionary from list:", my_dict_from_list)

#convert dictionary to list
dict_values = list(my_dict.values())  # Converting dictionary values to a list
print("Dictionary values as list:", dict_values)

keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']

my_dictionary = {k: v for k, v in zip(keys, values)}
print(my_dictionary)

#three different dict variable
d1 = {"a":4,"b":8,"d":56}
d2 = {"a":4,"b":8,"c":56}
d3 = {"a":4,"b":8,"g":56}

# Using setdefault to ensure key 'c' exists with value 100 if not present
d1.setdefault('c', 100)
d2.setdefault('c', 100)
d3.setdefault('c', 100)

print("d1:", d1)
print("d2:", d2)
print("d3:", d3)

print("***********other data structures***********")
# 6. Array (using the array module)
# import array
# my_array = array.array('i', [1, 2, 3, 4, 5])
# print("Array:", my_array)

# # 7. Bytearray
# my_bytearray = bytearray(b"Hello")
# print("Bytearray:", my_bytearray)

# 8. Frozenset
print("************frozenset**********")
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", my_frozenset)
# Frozenset is an immutable version of a set. Once created, its elements cannot be changed, added, or removed.
# Frozensets are useful as dictionary keys or set elements because they are hashable.

# Example operations with frozenset:
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

print("Frozenset 1:", fs1)
print("Frozenset 2:", fs2)

# Union
print("Union:", fs1 | fs2)

# Intersection
print("Intersection:", fs1 & fs2)

# Difference
print("Difference (fs1 - fs2):", fs1 - fs2)

# Symmetric Difference
print("Symmetric Difference:", fs1 ^ fs2)

# Membership test
print("Is 2 in fs1?", 2 in fs1)

# Frozensets can be used as dictionary keys
frozenset_dict = {fs1: "first", fs2: "second"}
print("Dictionary with frozenset keys:", frozenset_dict)

print("***********range***********")
# 9. Range
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number.
# range(start, stop, step)
# Range objects are immutable sequences of numbers commonly used for looping a specific number of times in for-loops.

# Example 1: range with only stop
r1 = range(5)  # 0, 1, 2, 3, 4
print("range(5):", list(r1))

# Example 2: range with start and stop
r2 = range(2, 7)  # 2, 3, 4, 5, 6
print("range(2, 7):", list(r2))

# Example 3: range with start, stop, and step
r3 = range(1, 10, 2)  # 1, 3, 5, 7, 9
print("range(1, 10, 2):", list(r3))

# Example 4: range with negative step
r4 = range(10, 0, -2)  # 10, 8, 6, 4, 2
print("range(10, 0, -2):", list(r4))

# Example 5: using range in a for loop
print("Using range in a for loop:")
for i in range(3):
    print("Iteration:", i)

# # 9. Deque (using collections module)
# from collections import deque
# my_deque = deque([1, 2, 3, 4, 5])
# print("Deque:", my_deque)

# 10. NamedTuple (using collections module)
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# my_namedtuple = Point(10, 20)
# print("NamedTuple:", my_namedtuple)

# 11. DefaultDict (using collections module)
# from collections import defaultdict
# my_defaultdict = defaultdict(int)
# my_defaultdict['a'] += 1
# print("DefaultDict:", my_defaultdict)

# 12. OrderedDict (using collections module)
# from collections import OrderedDict
# my_ordereddict = OrderedDict()
# my_ordereddict['a'] = 1
# my_ordereddict['b'] = 2
# print("OrderedDict:", my_ordereddict)

# 13. Counter (using collections module)
# from collections import Counter
# my_counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
# print("Counter:", my_counter)

# 14. ChainMap (using collections module)
# from collections import ChainMap
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# my_chainmap = ChainMap(dict1, dict2)
# print("ChainMap:", my_chainmap)

# 15. Heapq (using heapq module)
# import heapq
# my_heap = [3, 1, 4, 1, 5, 9]
# heapq.heapify(my_heap)
# print("Heap (after heapify):", my_heap)
# print("Smallest element in heap:", heapq.heappop(my_heap))

# 16. PriorityQueue (using queue module)
# from queue import PriorityQueue
# my_priority_queue = PriorityQueue()
# my_priority_queue.put((2, 'task 2'))
# my_priority_queue.put((1, 'task 1'))
# my_priority_queue.put((3, 'task 3'))
# print("PriorityQueue elements:")
# while not my_priority_queue.empty():
#     print(my_priority_queue.get())


# 17. Stack (using list)
# my_stack = []
# my_stack.append(1)
# my_stack.append(2)
# my_stack.append(3)
# print("Stack (after pushing 1, 2, 3):", my_stack)
# print("Popped from stack:", my_stack.pop())
# print("Stack (after pop):", my_stack)

# 18. Queue (using queue module)
# from queue import Queue
# my_queue = Queue()
# my_queue.put(1)
# my_queue.put(2)
# my_queue.put(3)
# print("Queue (after enqueueing 1, 2, 3):", list(my_queue.queue))
# print("Dequeued from queue:", my_queue.get())
# print("Queue (after dequeue):", list(my_queue.queue))


# user_details = {
#     'admin': {'david': 1234, 'john': 5678},
#     'staff': {'alice': 1111, 'bob': 2222}
# }

# dept = input("Enter department (admin/staff): ")
# if dept in user_details.keys():
#     print("your department is:", dept)
#     if dept == 'admin' or dept == 'staff':
#         print("Admin users:", list(user_details[dept].keys()))
#     username = input("Enter username: ")
#     if username in user_details[dept]:
#         password = int(input("Enter password: "))
#         if user_details[dept][username] == password:
#             print("Access granted.")
#         else:
#             print("Access denied. Incorrect password.")
#     else:
#         print("Access denied. Username not found.")

