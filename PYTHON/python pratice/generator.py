#A generator function is a special type of function that returns an iterator object. 
#Instead of using return to send back a single value, generator functions use yield to produce a series of results over time
def count_up_to(n):
    count = 1
    while count <= n:
        yield count #yeild is generator retuen value its lazy execute step by step
        count += 1

# Example usage:
for number in count_up_to(5):
    print(number)

def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b #here a+b add value assign value for b then updated b value added to a value thats itt enjoy
 
# Example usage:
for num in fibonacci_series(20):
    print(num)

# Using all() and any() functions with generators

# Check if all numbers in the generator are even
even_numbers = (x % 2 == 0 for x in range(2, 11))
print("All numbers are even:", all(even_numbers)) #false not every num is even

# Check if any number in the generator is divisible by 5
numbers = (x for x in range(1, 11))
print("Any number divisible by 5:", any(x % 5 == 0 for x in numbers))