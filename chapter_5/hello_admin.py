#usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a report?")
        else:
            print(f"Hello {user}, thank youj for logging in again")
else:
    print("We need to find some users")
