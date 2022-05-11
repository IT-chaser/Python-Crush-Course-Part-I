filename = 'programming_pol.txt'
poll = 0
while True:
    print("Enter 'quit' to exit")
    poll = input("Please enter the reason why you like programming: ")
    if poll == 'quit':
        break
    with open(filename, 'a') as file_object:
        file_object.write(f"{poll}\n")
