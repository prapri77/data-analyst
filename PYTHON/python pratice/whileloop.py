i=0
while i<5:
    print(f"{i}")
    i+=1

else:
    print("loop ends")

# Using break in a while loop
j = 0
while j < 5:
    if j == 3:
        break
    print(f"break example: {j}")
    j += 1

# Using continue in a while loop
k = 0
while k < 5:
    k += 1
    if k == 2:
        continue #it will skip the conditions
    print(f"continue example: {k}")

l1 = [1,2,4,6,7,56,87,78]

i = 0
#while using list
while i<len(l1):
    print(l1[i])
    print(l1[i]*2)
    print()
    i+=1
else:
    print("list ends")

#nested while loop

l2d =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(len(l2d))
i=0
while i < len(l2d):
    print("main row array")
    # print(l2d[i])
    row = l2d[i]
    print(row)

    j=0
    while j < len(row):
        # print(len(row))
        print("sub row elements array")
        print(row[j])
        j+=1
    i+=1
    print("$$$$$$$$$$")
else:
    print("l2d ends")

user_details = {
    'admin': {'raja': 1234, 'saran': 5678},
    'staff': {'ahmed': 1111, 'imran': 2222}
}
chances = 3
login_success = 0
while chances and not login_success:
    dept = input("Enter department (admin/staff): ")
    if dept in user_details.keys():  #checking dept
        print("your department is:", dept) #dept name display
        print("admin or staff users:", list(user_details[dept].keys())) #listing out admin/staff users
        username = input("Enter username: ") 
        cred_chances = 3 # this cred_chances for password 
        if username in user_details[dept]:
            while cred_chances: #nested while loop
                password = int(input("Enter password: "))
                if user_details[dept][username] == password:
                    print(f"Access granted.....welcome to {username} {dept}!!!")
                    login_success = 1 #exit from outer loops after value become true
                    break #break the inner loops
                else:
                    # print("Access denied. Incorrect password.")
                    cred_chances-=1
                    print(f"password correction check {cred_chances} times available")
            else:
                print()
                print("cred_chances over try to remember and login again sir")
        else:
            print("Access denied. Username not found.")
    else:
        print("dept name is wrong enter correctly")
    #  print("admin/staff team password is wrong")
    chances -= 1
    if chances and not login_success :
        print(f"dept correction check {chances} times available")
#after successfully login we comes  to homepage    
if login_success:
    while True:
        print("$$$$Home page$$$$")
        if dept == "admin" or dept == "staff":
            print("1.view admin users")
            print("2.view staff users")
            print("3.logout")
            choice = input("choose an options[1:3]: ") 

            if choice == '1':
                print(" admin users:")
                for username in user_details['admin']:
                    print(f"- {username}")
                break    
            elif choice == '2':
                print(" staff users:")
                for username in user_details['staff']:
                    print(f"- {username}")
                break    
            elif choice == '3':
                print("logout successfully")
                break
print(" visited this home page successfully")

# else:
#     print("chances over exit and try agin please")
    


