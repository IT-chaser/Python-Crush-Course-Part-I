cats_dogs = ['cats.txt', 'dogs.txt']
for cat_dog in cats_dogs:
        try:
            with open(cat_dog) as f:
                contents = f.read()
        except FileNotFoundError:
            print("Sorry file doesn't exist")
        else:
            print(contents.title())
