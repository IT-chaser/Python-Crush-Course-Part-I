favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
people = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in people:
        print(f"Dear {name.title()}, thank you for responding!")
    else:N
        print(f"Dear {name.title()}, We invite you to take th poll")