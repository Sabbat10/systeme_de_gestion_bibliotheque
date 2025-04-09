from ..data.data import list_users

def myUser():
    """
    Function to display user information.
    """
    for user in list_users:
        print(f"Name: {user['name']}")
        print(f"First Name: {user['fist_name']}")
        print(f"Age: {user['age']}")
        print(f"Email: {user['email']}")
        print(f"Password: {user['password']}")
        print("\n")