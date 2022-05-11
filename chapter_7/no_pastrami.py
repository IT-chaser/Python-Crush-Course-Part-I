sandwich_orders = ['tuna', 'pastrami', 'potato', 'pastrami', 'cheese', 'beef',
    'pastrami']
print("Deli has run out of pastrami")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami':
        print(f"I made your {sandwich.title()} sandwich\n")
        finished_sandwiches.append(sandwich)
print("---Fineshed Sandwiches---\n")
for finished_sandwich in finished_sandwiches:
    print(f"The {finished_sandwich.title()} sandwich has been made\n")
