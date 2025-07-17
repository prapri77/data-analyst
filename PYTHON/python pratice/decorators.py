import time

# Example 1: Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator #how we assign decorators
def say_hello():
    print("Hello!") #this a actual function will go to decorators as arguments func

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Example 2: Decorator with Arguments
def repeat(n): #n=3
    def decorator(func): #here def greet function goes
        def wrapper(*args, **kwargs): 
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# Example 3: Decorator for Timing Functions

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
# Output:
# Executed in 1.000x seconds

def validator(func):
    def verify(user):
        username = ['prasanth','priya','mari']
        if user in username:
            print(f"welcome to access your work")
            func(user)
        else:
            print(f"authencation failed")
    return verify
    

@validator
def auth(user):
    print(f"welcome mister {user}!!! verification done")
auth("prasanth")