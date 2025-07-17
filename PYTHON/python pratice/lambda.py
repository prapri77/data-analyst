#lambda function
# Example 1: Add two numbers
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Example 2: Square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Example 3: Sort a list of tuples by the second element
pairs = [(1, 3), (2, 2), (4, 1)]
pairs.sort(key=lambda pair: pair[1]) #(1,3) here 3 value is accessed for sorting means index of 1
print(pairs)  # Output: [(4, 1), (2, 2), (1, 3)]

# Example 4: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

from functools import reduce
from itertools import accumulate
l1 = ['apple','kiwi','orange','pineapple','dragonfruit']
l1.sort(key= lambda x:len(x)) #here sorting based on len
#filter
res = list(filter(lambda x: "a" not in x, l1))
#map [function,iteration]
res1 = list(map(lambda x: x+" juice", l1))

#reduce
num2= [1, 2, 3, 4, 5, 6]
n1= reduce(lambda x,y:x+y, num2) #reduce give cumulative value or single value result 
n2= accumulate(num2, add)
print(l1)
print(res)
print(res1)
print(n1)
print(list(n2))

#comprehension with lambda
#[(lambda_expression)(item) for item in iterable]
x= [(lambda x: x*2)(i) for i in range(7)]
print(x)
