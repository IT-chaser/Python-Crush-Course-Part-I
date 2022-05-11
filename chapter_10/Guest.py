filename = 'guest.txt'
with open(filename, 'w') as file_object:
    user_name = input("Please enter your name here: ")
    file_object.write(user_name)
    print(f"Great! Your name is added to {filename} file as {user_name}")
