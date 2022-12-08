#create a calculator:
#Data (variable): first , second , result
#Opeartions(function) : add , sub , div , mul,accept ,
#display, menu

#Scope of a variable :
#Global Scope : data changed be changed
#local scope : data can be accessed inside the block


#defining the variable in global scope
first , second , result = 0, 0 ,0

#Modular Programming : break a complex code into
#small individual unit of code

#accept fuction
def acceptData():
    global first
    global second
    
    print("Enter first number : ")
    first = int(input())
    print("Enter second number : ")
    second = int(input())

    
#display function
def displayResult():
    print("Result of the calculation is :" , result)


def add():
    global result
    result = first + second

def sub():
    global result
    result = first - second

def mul():
    global result
    result = first * second

def div():
    global result
    global second

    while(second == 0):
        print("!!Division not possible as the second number is zero!!!")
        print("enter second number :")
        second = int(input())

    result = first / second

def menu():
    print("----------------CALCULATOR MENU----------------")
    print("1. Add")
    print("2. Sub")
    print("3. Div")
    print("4. Mul")
    print("------------------------------------------------")
    ch = int(input())
    
    acceptData()
    
    if ch == 1:
        add()
    elif ch == 2:
        sub()
    elif ch == 3:
        div()
    elif ch == 4:
        mul()
    else:
        print("Incorrect input")

    displayResult()

    print("\nDo you want to continue(Y/N) : ")
    ch = input().upper()
    if ch =="Y":
        menu()
    else:
        print("\nThankYou\n")
    
menu()
    

