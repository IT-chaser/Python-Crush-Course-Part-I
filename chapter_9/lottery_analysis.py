from random import choice
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [1, 4, 'a', 'e']
selected = []
attempts = 0
while len(selected) < 4:
    attempts += 1
    random = choice(lottery)
    if random in my_ticket:
        lottery.remove(random)
        selected.append(random)
print(f"Number of attempts: {attempts}")

print(f"Selected lottery numbers are {selected}")
print(lottery)
