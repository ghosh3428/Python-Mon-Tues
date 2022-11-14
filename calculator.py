#global variable
first , second = 10, 0
result = 0

#defiune a function
def add():
    global result
    result = first + second

def sub():
    global result
    result = first - second

def div():
    global result
    global second
    while second == 0:
        print("Error : Division not possible as the second number is zero.")
        print("Please enter a new value : ")
        second = int(input())
    result = first // second

def mul():
    global result
    result = first * second


def menu():
    global first
    global second
    print("-------------CALCULATOR MENU--------------")
    print("1. Add")
    print("2. Sub")
    print("3. Div")
    print("4. Mul")
    print("-----------------------------------------")
    ch = int(input())

    print("Enter two numbers : ")
    first = int(input())
    second = int(input())

    if ch == 1:
        add()
    elif ch == 2:
        sub()
    elif ch == 3:
        div()
    elif ch ==4:
        mul()

    print("\nResult of calculation is :" ,result)



#calling the function
menu()


