try:
    age = int(input("Enter a number to divide: "))
    result = 100/ age
    print(result)
except ValueError:
    print("Error please enter a valid number")
except ZeroDivisionError:
    print("Age cannot be zero")
except Exception as e:
    print(e)
finally:
    print("finally block")

def check_length(password):
    if len(password) < 5:
        raise ValueError("Error password length must be minimum of 5")
    return True

try:
    password = input("Enter the password: ")
    check_length(password)
except ValueError as error_message:
    print(error_message)

users = [{"name": "vk", "mobile": "24123123"}, {"name": "new", "mobile": "21323"}]

for user in users:
    try:
        print(f"The email id of person is {user['email']}")
    except KeyError:
        print(f"The Variable Email ID for {user['name']} doesn't exist")    
