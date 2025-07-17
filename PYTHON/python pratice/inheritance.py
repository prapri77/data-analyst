#OPERATORS OVERLOADING
# Python Program illustrate how 
# to overload an binary + operator
# And how it actually works

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects 
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2)) 
print(A.__add__(ob3,ob4)) 
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

#METHOD OVERRIDING PROCEES:
#The Child class overrides the show() method of the Parent class, so when show() is called on an instance of Child, 
# it uses the Child class’s implementation.

class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		super().__init__()  # Call parent constructor
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) #HERE IT OVERIDE PARENTS 
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"


#SINGLE LEVEL INHERITANCE:A child class inherits from one parent class.
class Animal:
    def info(self):
        print("Animals are living organisms that feed, move, and reproduce.")

    def classification(self):
        print("Animals are classified into various groups based on their characteristics.")

class LandAnimals(Animal):
    def land_info(self):
        Animal.info(self)
        print("Land animals live primarily on land.")

# Example usage
animal = Animal() #base or super class
animal.info()
animal.classification()

land_animal = LandAnimals() #derived or sub class
# land_animal.info()           # Inherited from Animal
land_animal.classification() # Inherited from Animal
land_animal.land_info()      # Defined in LandAnimals

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())

#SUPER FUNCTION:It allows you to call methods defined in the superclass from the subclass
class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add

# Class freelancer inherits EMP 
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add) #THIS WILL GO TO BASE CLASS CONSTRUCTORS OR ANY FUN IN SUPER CLASS
        self.Emails = Emails

Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "abc@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

#MULTIPLE INHERITANCE:  A child class inherits from more than one parent class.

class A:
    def showA(self):
        print("This is class A")

class B:
    def showB(self):
        print("This is class B")

class C(A, B):  # multiple inheritance here a,b is base class of child class c
    def showC(self):
        print("This is class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()

#MULTILEVEL INHERITANCE A class is derived from a class which is also derived from another class.
#Grandparent → Parent → Child
class Grandfather:
    def house(self):
        print("Grandfather: Owns a big house")

class Father(Grandfather):
    def car(self):
        print("Father: Owns a car")

class Son(Father):
    def laptop(self):
        print("Son: Uses a laptop")

# Create object of Son
s = Son()
s.house()    # Inherited from Grandfather
s.car()      # Inherited from Father
s.laptop()   # From Son

#Hierarchical Inheritance: Multiple classes inherit from a single parent class.
class Parent:
    def show(self):
        print("This is Parent class")

class Child1(Parent):
    def feature1(self):
        print("Feature of Child1")

class Child2(Parent):
    def feature2(self):
        print("Feature of Child2")

# Create objects of each child
c1 = Child1()
c2 = Child2()

c1.show()       # From Parent
c1.feature1()   # Specific to Child1

c2.show()       # From Parent
c2.feature2()   # Specific to Child2

#Hybrid Inheritance: A combination of more than one type of inheritance.
class A:
    def showA(self):
        print("Class A")

class B(A):  # Single Inheritance
    def showB(self):
        print("Class B")

class C(A):  # Hierarchical Inheritance
    def showC(self):
        print("Class C")

class D(B, C):  # Multiple Inheritance
    def showD(self):
        print("Class D")

obj = D()
obj.showA()  # From A
obj.showB()  # From B
obj.showC()  # From C
obj.showD()  # From D

#COMBINATION OF ALL INHERITANCE TYPES:
# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)            # Initialize Job

# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.department = department

# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size

# 5. Hybrid Inheritance ( Multilevel + Hierarchical Inheritance )
class SeniorManager(Manager, AssistantManager):  # Inherits from both Manager and AssistantManager
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        # Initialize Manager
        AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager

# Creating objects to show inheritance

# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)

# Hierarchical Inheritance
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)

class a :
    def add(self):
        return self.a + self.b
    
class b(a):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def math(self):
        print(a.add(self))
        return self.a - self.b

su = b(4,2)
print(su.math())

class a :
    def __init__(self):
        pass
    
class b(a):
    def __init__(self,a,b): #here constructor override super class a only sub class execute
        self.a = a
        self.b = b
    def math(self):
        # print(a.add(self))
        return self.a - self.b

su = b(4,2)
print(su.math())

#OVERLOADING
def product(a,b,c):
    return a*b*C

def product(a,b):
    return a*b

# print(product(3,6,7)) here 2nd fun only execute
print(product(3,6))

#to avoid overloading problem in fun we use dispatch
from multipledispatch import dispatch

@dispatch (int,int, int)
def product(a,b,c):
    return a*b*c

@dispatch(int,int)
def product(a,b):
    return a*b

print(product(3,6,7))
# print(product(3,6,7)) here 2nd fun only execute
print(product(3,6))

#for class we use this
class Parent:
    def show(self):
        print("This is Parent class")

class Child1(Parent):
    def feature(self):
        print("Feature of Child1")

class Child2(Parent):
    def feature(self):
        # Child1.feature(self) #overloading 
        print("Feature of Child2")

fe = Child2()
print(fe.feature())

#operator overloading
class Test:
    def __init__(self, x): #here 10
        self.x = x

    def __add__(self, other): #here 20
        return self.x + other.x, self.x-other.x

t1 = Test(10)
t2 = Test(20)
print(t1+t2)

class TestSum:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def fun(self):
        if self.a is not None and self.b is not None and self.c is not None:
            return self.a + self.b + self.c
        elif self.a is not None and self.b is not None:
            return self.a + self.b
        elif self.a is not None:
            return self.a
        else:
            return None

# Example usage:
t1 = TestSum(1, 2, 3)
print(t1.fun())  # 6

t2 = TestSum(4, 5)
print(t2.fun())  # 9

t3 = TestSum(7)
print(t3.fun())  # 7

t4 = TestSum()
print(t4.fun())  # None


class ClassA:
    def show(self):
        print("This is ClassA")

class ClassB:
    def show(self):
        print("This is ClassB")

class ClassC:
    def show(self):
        print("This is ClassC")

class ClassD:
    def show(self):
        print("This is ClassD")

classes = [ClassA(), ClassB(), ClassC(), ClassD()]
for obj in classes:
    obj.show()









