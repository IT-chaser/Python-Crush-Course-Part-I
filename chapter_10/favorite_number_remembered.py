import json

#Load the favorite number if it has been stored previously.
#Otherwise, prompt for the username and store it.
file_name = 'favorite_number.json'
try:
    with open(file_name) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    fav_num = input("What is your favorite number? ")
    with open(file_name, 'w') as f:
        json.dump(fav_num, f)
        print(f"We'll remember your favorite number {fav_num}.")
else:
    print(f"Your favorite number is {fav_num}")
