import json
fav_num = input("What is your favorite number? ")
file_name = 'favorite_number.json'
with open(file_name, 'w') as f:
    json.dump(fav_num, f)
