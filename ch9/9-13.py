from random import randint

class Die:
    
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self, times = 10):
        for i in range(0, times + 1):
            print(randint(1, self.sides), end = ' ')
        print()


die1 = Die()
die1.roll_die()

die2 = Die(10)
die2.roll_die()

die3 = Die(20)
die3.roll_die()
