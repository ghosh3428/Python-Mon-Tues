#Write a Python program to generate a random color hex,
#a random alphabetical string,
#random value between two integers (inclusive) and
#a random multiple of 7 between 0 and 70.

#Write a Python function that accepts a string and
#calculate the number of uppercase letters and
#lower case letters.


import random
import string


def colorCode():
    myrange = "0123456789ABCDEF"
    hexcode = "#" + "".join(random.sample(myrange , 6))
    print("Random Color Code:" , hexcode)

def alphaString():
    data = ""
    for i in range(255):
        data = data + random.choice(string.ascii_letters)
    print("Random Alphabetical String :",data)

def randomNumber():
    upper = int(input("Enter Upper Limit : "))
    lower = int(input("Enter Lower Limit : "))
    data = random.randint(lower,upper)
    print("Random number is :" , data)
    
def randomMultiple():
    data = (random.randint(0,10))*7
    print("Random multiple of 7 between 0 and 70 :" , data)

def lowercase():
    data = input("Enter a sentence : ")
    lcount=0
    for i in data:
        if(i.islower()):
            lcount = lcount + 1

    print("Number of lower case letters is:",lcount)

def uppercase():
    data = input("Enter a sentence : ")
    ucount=0
    for i in data:
        if(i.isupper()):
            ucount = ucount + 1

    print("Number of upper case letters is:",ucount)

    
def menu():
    print("-----------------RANDOM MENU-------------")
    print("1. Random Color Hex-Code")
    print("2. Randon Alphabetical String")
    print("3. Random number")
    print("4. Random multiple of 7 between 0 and 70")
    print("5. Calculate UpperCase")
    print("6. Calculate LowerCase")
    print("-----------------------------------------")

    ch = int(input())
    if ch == 1:
        colorCode()
    elif ch == 2:
        alphaString()
    elif ch == 3:
        randomNumber()
    elif ch == 4:
        randomMultiple()
    elif ch == 5:
        uppercase()
    elif ch == 6:
        lowercase()


menu()



    

