#class object calling
class test:
    var1 = 'apple'
    var2 = 'orange'
    def add(self):
        self.var3 = 55
        return self.var1 + self.var2
    
obj = test()
print("add:",obj.add())
print(obj.var3)

#constructors
class example:
    def __init__(self, name, age):#obj created it calls fun
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}") #then prints display fun

obj = example("Alice", 30)
obj.display()

#arthimatic operation using class
class test:
    def __init__(self, a, b): #it initialise when obj created constructors
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:#to avoid error of zero divisional value
            return self.a / self.b
        else:
            return "Division by zero error"

    def all_operations(self): #self is the instance method
        return {
            'add': self.add(),
            'subtract': self.subtract(),
            'multiply': self.multiply(),
            'divide': self.divide()
        }

# Example usage:
obj = test(10, 5)
print(obj.all_operations())

#@property ans special method __str__
class Demo:
    def __init__(self, x, y): #self is the instance of the fun class
        self.x = x
        self.y = y

    @property #The @property decorator in Python is used to define getter methods in a class, so you can access a method like an attribute.
    def add(self):
        return self.x + self.y

    def __str__(self): #this fun it print when object print
        return f"Demo(x={self.x}, y={self.y}, add={self.add})"

# Example usage:
obj = Demo(7, 3)
print(obj)
print("Addition using @property:", obj.add) #here we call function without parenthesis by @property

class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

p = Person(25)
print(p.age)     # 25
p.age = 30       # uses setter
print(p.age) 
del p.age        # uses deleter

#@static method is general function without self instance
#In Python, @staticmethod is a decorator used to define a static method inside a class — 
# a method that doesn’t access or modify the class (cls) or instance (self) data.

class Demo:
    def instance_method(self): #self instance method
        print("I am an instance method")

    @classmethod
    def class_method(cls): #cls method
        print("I am a class method")

    @staticmethod
    def static_method():#static method
        print("I am a static method")

d = Demo()
d.instance_method()   # needs self
d.class_method()   # needs cls
d.static_method()  # no self/cls

#class method takes cls as the first argument instead of self.
class person:
    species = "humans"

    @classmethod
    def cls_species(cls,new_sps):
        cls.species = new_sps

p = person()
print("before:",p.species) #its normal varaiable
p.cls_species("superhumans")
print("after:",p.species)#its a cls variable

#override values examples
class A:
    x=67
    y=78
    def add(self,a): #here we pass argument but it taks only variable x and y overide not happens
        self.sum = self.x + self.y
    def sub(self,a):
        self.subraction = self.x - self.y

ob = A()
print(ob.add(678))
print(ob.sum)
print(ob.sub(67))
print(ob.subraction)

class B:
    x=67
    y=78
    def add(self,x): #here we pass argument but it taks only variable
        self.x = x #how we override x = 678 value,because actual value is 67
        self.sum = self.x + self.y

ob = B()
print(ob.add(678))
print(ob.sum)

#reinitiating a value using class or updating variable

class Person:
    def __init__(self, firstname, ocountry):
        self.name = firstname
        self.country = ocountry

    def fullname(self, lname):
        self.name = self.name + lname
        return self.name

    def address(self, city):
        self.country = self.country + city
        return self.country

# Example usage:
p = Person("John", "US")
print(p.name) #intialise
print(p.country) #intialise
print(p.fullname(" Doe"))
print(p.address(" new york"))
print(p.name) #reinitialise
print(p.country) #reinitialise happens

class profile:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# Creating an object and overriding values
p = profile("Jane", "Smith")
print(p.firstname, p.lastname)
print(p.firstname)

# Overriding the values
p.firstname = "Emily"
p.lastname = "Johnson"
print(p.firstname, p.lastname)
print(p.firstname)





