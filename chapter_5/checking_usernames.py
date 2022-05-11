current_users = ["user1", 'user2', 'user3', 'user4', 'user5']
new_users = ['USER1', 'nuser2', 'user3', 'nuser4', 'nuser5']
existing_users = current_users
for new_user in new_users:
    if new_user.lower() in existing_users:
        print(f"This {new_user} is already taken, Please select different name")
    else:
        print(f"This {new_user} is available")