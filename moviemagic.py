year , title , rating = 0,"",0.0

def accept():
    global year
    global rating
    global title

    year = int(input("Enter movie year : "))
    title = input("Enter movie title : ")
    rating = float(input("Enter movie rating between 0.0 and 5.0 : "))

    while rating<0.0 or rating>5.0 :
        print("!!!Error : Invalid Rating !!!")
        print("Please enter a valid rating")
        rating = float(input())


def display():
    print("Movie Title : " ,title)
    print("Movie Year : " ,year)
    print("Movie Rating : " ,rating)

    if(rating>=0 and rating <=2.0):
        print("It is a Flop Movie")
    elif(rating>=2.1 and rating <=3.4):
        print("It is a Semi-Hit Movie")
    elif(rating>=3.5 and rating <=4.5):
        print("It is a Hit Movie")
    elif(rating>=4.6 and rating <=5.0):
        print("It is a Super-Hit Movie")

for i in range(2):
    accept()
    display()
    print("\n\n")