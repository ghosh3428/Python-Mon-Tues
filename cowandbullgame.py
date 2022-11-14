import random
rData = "".join(random.sample("1234567890" , 4))
uData = input("Guess a number between 1000 and 9999 : ")
while rData != uData:
    print("!!!Incorrect Guess!!!")
    cow , bull = 0 ,0 
    #range(start , end , step)
    #default value of start = 0
    #default value of step = 1
    for i in range(4):
        if uData[i] == rData[i]:
            cow = cow + 1
        else:
            if uData[i] in rData:
                bull = bull + 1

    print("Cow : " , cow)
    print("Bull : " , bull)

    print("Guess a new value :")
    uData=input()

print("Correct Guess..... You have won the game")

