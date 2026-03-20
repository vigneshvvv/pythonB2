user_detail = [
    {"userName": "alice", "password": "alice"},
    {"userName": "bob", "password": "bob"}
]

def check_login(user_detail, userName, password):
    for user in user_detail:
        if user["userName"] == userName and user["password"] == password:
            return True
        
    return False   

def login_input():
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")
    if check_login(user_detail, userName, password):
        return True
    else:
        return False

count = 1

while count <=3:
    if login_input():
        print("login successful! Welcome")
        break
    # elif count == 3:
    #     print("login failed")
    else:
        print("login failed please try again ")
    count +=1


def login_system():
    attempts = 0
    found = False
    while attempts <3:
        u = input("Enter your username: ")
        p = input("Enter your password: ")

        for user in user_detail:
            if user["userName"] == u and user["password"] == p:
                found = True
                print("success")
                break
        if not found:
            attempts +=1
            print(f"wrong! {3- attempts} left.")
        else:
            break
            
            
    else:
        print ("attempts exceeded")


login_system()



    
