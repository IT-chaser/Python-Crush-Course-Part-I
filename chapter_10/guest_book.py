filename = 'guest_book.txt'
user_name = 0
while True:
    print("Enter quit to exit")
    user_name = input("Please enter your name here: ")
    if user_name == 'quit':
        break
    with open(filename, 'a') as file_object:
        print(f"Hello dear {user_name.title()}!")
        file_object.write(f"{user_name.title()} viseted\n")
