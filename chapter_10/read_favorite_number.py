import json
filename = 'favorite_number.json'
with open(filename) as f:
    contents = f.read()
    print(f"I know your favorite number. it's {contents}")
