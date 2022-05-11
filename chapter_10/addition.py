print("Please enter two numbers, and we'll add them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("First number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("\nSorry, you can't add string value!")
    else:
        print(answer)
