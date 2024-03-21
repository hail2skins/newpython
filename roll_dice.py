import random

roll = random.randint(1, 6)

guess = int(input('Guess the dice roll:\n'))
if guess == roll:
    print('Correct! The roll was', roll)
else:
    print('Wrong! The roll was', roll)

