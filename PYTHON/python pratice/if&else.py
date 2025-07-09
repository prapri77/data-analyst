x = 1
if x > 5:
    print("x is greater than 5")
else:
    print("x is smaller than 5")

y = 5
if y < 5:
    print("y is less than 5")
elif y == 5:
    print("y is equal to 5")
else:
    print("y is greater than 5")


z = 20  # global variable

def check_variable():
    a = 15  # local variable
    if z > 10:
        print("Global variable z is greater than 10")
    if a > 10:
        print("Local variable a is greater than 10")
    return a
    

d = check_variable()
print("Accessing global variable z outside function:", z)
# The following line would cause an error if uncommented, since 'a' is local to the function
print(d)

num = 12

if num > 0:
    print("Number is positive")
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is not positive")

a = "python" 
if "t" in a: print("exists")

list1 = [1, 2, 3]
list2 = [5,7,8]
list3 = [9,8,6]

print("list1 is big") if list1>list2 else print("list2 is big") if list2>list3 else print("list3 is big")

assert 4 ** 4 == 256
print("successful")

# Example of assert syntax:
# assert <condition>, <optional error message>

value = 10
assert value > 5, "Value must be greater than 5"
print("Assertion passed: value is greater than 5")

# user_details = {
#     'admin': {'david': 1234, 'john': 5678},
#     'staff': {'alice': 1111, 'bob': 2222}
# }

# dept = input("Enter department (admin/staff): ")
# if dept in user_details.keys():
#     print("your department is:", dept)
#     if dept == 'admin' or dept == 'staff':
#         print("Admin or staff users:", list(user_details[dept].keys()))
#     username = input("Enter username: ")
#     if username in user_details[dept]:
#         password = int(input("Enter password: "))
#         if user_details[dept][username] == password:
#             print("Access granted.")
#         else:
#             print("Access denied. Incorrect password.")
#     else:
#         print("Access denied. Username not found.")
# else:
#     print("dept name is wrong enter correctly")

