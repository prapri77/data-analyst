# Define a simple function that adds two numbers
def add_numbers(a, b):
    return a + b

# Example usage
result = add_numbers(5, 3)
print("The sum is:", result)

#parameters and args
def math(a,b):
    return a+b,a-b,a*b,a/b
r = math(3,4)

print("add", r[0])
print("sub", r[1])
print("mul", r[2])
print("div", r[3])

def math(a,b,c):
    return c-a-b

c = math(c=20,b=10,a=5)
print(c)

#oribitory postional args
def ct(*ar): #this positional arguments is a tuple
    print(min(ar))
    print(max(ar))
    print(sum(ar))
    print(len(ar))
    print(type(ar))
    return ar

obj = ct(1,2,3,4,5,7,89)
print(obj)

#keyword arguments dict data structure

def fun(**args):
    print(args.keys())
    print(args.values())
    print(type(args))
    return args

d = fun(c = 16,b ="hello",d = 25, h = "world")
print(d)

def fun(d1):
    for key in d1:
        print(f"keys:{key} values:{d1.get(key)}")
    return d1

d2 = fun({'c': 16, 'b': 'hello', 'd': 25, 'h': 'world'})
print(d2)

#default parameters functions
def pro(name = "user"):
    print("name",name)

pro()
pro("prasanth")

#recursive fun
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1) #here fact call funciton again and again for 4,3,2,1

f=fact(5)
print(f)
def fact(n):
    r =1
    for i in range(1,6):
        r*=i
    return(r)

s = fact(5)
print(s)

#local and global variable
y=107 #global variable 
def fun():
    print(y)
    #global x can used local access
    x=90 # variable local
    return x


f= fun() #local variable called using obj f 
print(f)

def o(): #outer fn
    def i(): #inner fn
        return 85+897
    return i() #here outer fn return inner fn values to object v

v = o()
print(v)

def ou(m):
    def inn(n):
        return m*n
    return inn(7)

r = ou(8)
print(r)

#zip,enumerator,fun,arguments,parameter,decorators,recursive,positional and keyword argument,default,outer inner fn


 
