import sys
import random

playerNumber = input("enter number between 1-100: \n")

player = int(playerNumber)
if player < 1 or player > 100:
    sys.exit("please enter number between 1-100")

computerNumber = random.randint(1, 100)
computer = int(computerNumber)
print(f"player guess : {player}")
print(f"computer guess : {computer}")

if player > computer:
    print("To heigh")
elif player < computer:
    print("to low")
elif player == computer:
    print("you won")
else:
    print("to close")
