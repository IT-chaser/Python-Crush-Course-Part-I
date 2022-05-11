with open('learning_python.txt') as file_object:
    #contents = file_object.read()
    #for line in file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip().title())
