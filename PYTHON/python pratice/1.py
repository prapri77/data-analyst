user_details = {
    'admin': {'raja': 1234, 'saran': 5678},
    'staff': {'ahmed': 1111, 'imran': 2222}
}

chances = 3
login_success = False  # Flag to exit all loops if login is successful

while chances and not login_success:
    dept = input("Enter department (admin/staff): ").lower()
    
    if dept in user_details:
        print("Your department is:", dept)
        print(f"Available users in {dept}:", list(user_details[dept].keys()))
        
        username = input("Enter username: ")
        cred_chances = 3
        
        if username in user_details[dept]:
            while cred_chances:
                try:
                    password = int(input("Enter password: "))
                except ValueError:
                    print("Please enter a numeric password.")
                    continue
                
                if user_details[dept][username] == password:
                    print("✅ Access granted.")
                    login_success = True
                    break  # exit password loop
                else:
                    cred_chances -= 1
                    print(f"❌ Incorrect password. {cred_chances} attempts left.")
            else:
                print("🚫 Too many incorrect attempts. Try again later.")
        else:
            print("❌ Access denied. Username not found.")
    else:
        print("❌ Department name is wrong. Enter correctly.")
    
    chances -= 1
    if not login_success and chances:
        print(f"🔁 You have {chances} department-level attempt(s) left.")

if not login_success:
    print("❌ All chances exhausted. Exiting...")
