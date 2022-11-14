#Write a Python program to generate a
#1) random color hex,
#2) a random alphabetical string,
#3) random value between two integers (inclusive) and
#4) a random multiple of 7 between 0 and 70.

import random
import string

def colorCode():
    mylist = "1234567890ABCDEF"
    colorcode = "#"
    for i in range(6):
        colorcode = colorcode + random.choice(mylist)

    print("Random Color Hex Code :" , colorcode)

def alphaString():
    mystring = ""
    for i in range(255):
        mystring = mystring+random.choice(string.ascii_letters)

    print("Random Alpha String :" , mystring)

def randomNumber():
    lower = int(input("Enter the lower limit : "))
    upper = int(input("Enter the upper limit : "))

    print("Random number between lower and upper is :",random.randint(lower , upper))
    
def randomMultiple():
    data = (random.randint(0,10))*7
    print("Random multiple of 7 between 0 and 70 is :",data)
    
def menu():
    print("----------------RANDOM MENU----------------")
    print("1. Color Code")
    print("2. Aplhabetical String")
    print("3. Random number")
    print("4. Random Multiple of 7")
    print("------------------------------------------------")
    ch = int(input())

    if ch == 1:
        colorCode()
    elif ch == 2:
        alphaString()
    elif ch == 3:
        randomNumber()
    elif ch == 4:
        randomMultiple()
    else :
        print("\nInvalid Input\n")

    print("\nDo you want to continue(Y/N) : ")
    ch = input().upper()
    if ch =="Y":
        menu()
    else:
        print("\nThankYou\n")


menu()

    
