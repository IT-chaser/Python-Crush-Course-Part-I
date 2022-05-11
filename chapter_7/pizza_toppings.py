prompt = ("\nPlease enter your desired pizza toppings:")
prompt += ("\nEnter 'quit' to end the program. ")
pizza_toppings = ""
while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)
    if pizza_toppings != 'quit':
        print(f"We will add this {pizza_toppings} in to your pizza")
