sandwich_orders = ['tuna', 'potato', 'cheese', 'beef']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich.title()} sandwich\n")
    finished_sandwiches.append(sandwich)
print("---Fineshed Sandwiches---\n")
for finished_sandwich in finished_sandwiches:
    print(f"The {finished_sandwich.title()} sandwich has been made\n")
