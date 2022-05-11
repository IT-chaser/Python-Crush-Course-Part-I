glossary = {'print': 'printing the values',
    'for loop': 'for looping throuth elements',
    'if condition': 'if statments for values',
    'list': 'list of values',
    'pop()': 'method for temporarly removing values',
    'del()': 'deleting list values',
    'len()': 'items count',
    'tuple': 'non modifiable elemnts',
    'dictionary': 'key/value associations',
    'range': 'integer sequances',
    }
for key, value in glossary.items():
    print(f"Key: {key.title()}")
    print(f"Value: {value.title()}\n")