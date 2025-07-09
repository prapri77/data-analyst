#basic project for department wise login using username and password

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
        print(f"{dept} users:", list(user_details[dept].keys())) #listing out admin/staff users
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
            if not login_success:
                print("Too many incorrect password attempts. Login failed.")
                login_success = 0 #after 3 time cred_chances over its redirect to all login exhausted
                break
        else:
            print("Access denied. Username not found.")
    else:
        print("dept name is wrong enter correctly")
        print()
        chances -= 1
    #  print("admin/staff team password is wrong")

    if chances and not login_success :
        print(f"dept correction check {chances} times available")
        print()
if not login_success:
    print("all login attempts exhausted. Exiting...") #failed conditions
#after successfully login we comes to homepage condition    
if login_success:
    while True:
        print("$$$$Home page$$$$")
        print("1.view admin users")
        print("2.view staff users")
        print("3.logout")
        choice = input("choose an options[1:3]: ") 

        if choice == '1' and dept == "admin": #if dept is admin only it will support this choice
            print(" admin users:")
            for username in user_details['admin']:
                print(f"- {username}")
            break
            
        elif choice == '2' and dept == "staff": #if dept is staff only it will support this choice
            print(" staff users:")
            for username in user_details['staff']:
                print(f"- {username}")
            break

        elif choice == '3':
            print("logout successfully")
            break

        else:
            print("invalid choice enter correct options")
            



    