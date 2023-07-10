import sys
import time
from random import randint


def game(score):
    print("0 - Head")
    print("1 - Tail")
    choice = (int(input()))
    if choice > 1 or choice < 0:
        print("Game over")
        sys.exit()
    win = randint(0, 1)
    if choice == win:
        print("coin flipping")
        time.sleep(1)
        print("You win")
        score[0] += 1
    else:
        print("coin flipping")
        time.sleep(1)
        print("You lose")
        time.sleep(1)
        score[1] += 1


scor = [0, 0]
print("Simple game. You need to choose, play till you lose. Let's go")
while scor[1] < 3:
    game(scor)
    if scor[1] == 3:
        print("You lose like a goose")
        print("Your final score: wins -", scor[0])
