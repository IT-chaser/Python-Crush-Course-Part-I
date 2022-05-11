with open('learning_python.txt') as file_object:
    contents = file_object.read()
    contents = contents.lower().replace('python', 'c')
    print(contents.title())
