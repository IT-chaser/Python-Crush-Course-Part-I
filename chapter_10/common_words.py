filename = 'Richmond.txt'
with open(filename, encoding='utf-8') as f:
    content = f.read()
    print(content.lower().count('park '))
