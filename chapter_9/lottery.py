from random import choice
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
selected = []
while len(selected) < 4:
    random = choice(lottery)
    lottery.remove(random)
    selected.append(random)
print(f"Selected lottery numbers are {selected}")
print(lottery)
