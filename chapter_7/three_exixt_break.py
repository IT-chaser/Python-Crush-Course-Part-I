prompt = ("\nPlease enter your age to know your ticket price:")
prompt += ("\nEnter 'quit' to end the program. ")
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if  age <= 3:
            print("Your ticket is free")
        elif age <= 12:
            print("Your ticket price is $10")
        elif age >= 12:
            print('Your ticket price is $15')
