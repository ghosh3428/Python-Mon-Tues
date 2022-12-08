studentList = list()

class Student:
    def __init__(self):
        self.dept = "Science"
        self.regNo = "R23000000100"
        self.m1 = 0
        self.m2 = 0
        self.m3=0
        self.m4 = 0
        self.total = 0
        self.avg = 0
        self.name = "New Student"

    def validateMarks(self , marks):
        while (marks <0 or marks>100):
            print("!!!Invalid marks !!!")
            print("Please enter a valid marks :")
            marks = int(input())

        return marks

        
    def accept(self):
        print("Enter student Name :")
        self.name = input()
        print("Enter Department :")
        self.dept = input()
        print("Enter Registration number :")
        self.regNo = input()
        print("Enter marks 1 :")
        self.m1 = int(input())
        self.m1 = self.validateMarks(self.m1)
        print("Enter marks 2 :")
        self.m2 = int(input())
        self.m2 = self.validateMarks(self.m2)
        print("Enter marks 3 :")
        self.m3 = int(input())
        self.m3 = self.validateMarks(self.m3)
        print("Enter marks 4 :")
        self.m4 = int(input())
        self.m4 = self.validateMarks(self.m4)

    def calculate(self):
        self.total = self.m1 + self.m2 + self.m3 + self.m4
        self.avg = round(self.total/4 , 2)
        
    def display(self):
        print("-----------------STUDENT DETAILS--------------")
        print("Student Name        :",self.name)
        print("Department Name     :",self.dept)
        print("Registration Number :",self.regNo)
        print("Marks 1             :",self.m1)
        print("Marks 2             :",self.m2)
        print("Marks 3             :",self.m3)
        print("Marks 4             :",self.m4)
        print("Total Marks         :",self.total)
        print("Average Marks       :",self.avg)
        print("-----------------------------------------------")


    

while(True):
    print("-----Student Menu----")
    print("1 . Add")
    print("2 . Display")
    print("3 . Search by Registration ID")
    print("0 . Exit")
    print("--------------------")

    i = int(input())
    if i ==0 :
        break
    elif i == 1:
        s1 = Student()
        s1.accept()
        for student in studentList:
            while student.regNo == s1.regNo:
                print("Registration Number already Present!!!")
                print("Enter a new value :")
                s1.regNo = input()
            
        s1.calculate()
        studentList.append(s1)
    elif i == 2:
        for student in studentList:
            student.display()
    elif i == 3:
        rid = input('Enter the id you want to search :')
        for student in studentList:
            if rid == student.regNo:
                student.display()
    else:
        print("Incorrect Option !!!")

    
