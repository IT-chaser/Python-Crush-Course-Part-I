from random import randint
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random = randint(1, self.sides)
        print(random)

die = Die(20)
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
die.roll_die()
