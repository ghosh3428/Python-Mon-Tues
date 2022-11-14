import random
rData = random.randint(0,9)
uData = int(input("Guess a number between 0 and 9 : "))
while rData != uData:
    print("!!!Incorrect Guess!!!")
    if uData < rData:
        print("Please guess a bigger number : ")
    else:
        print("Please guess a smaller number : ")
    uData = int(input())
print("Correct Guess..... You have won the game");