fo = open("phone.txt" , "r+")
while True:
    print("1. Read all Data")
    print("2. Add new Data")
    print("3. Search Data")
    print("4. Delete Data")
    print("5. Update Data")
    print("0. Exit")
    ch = int(input())

    if ch == 0:
        print("Thank You\n")
        break
    elif ch == 1:
        fo.seek(0,0)
        data = fo.read()
        print(data)

    elif ch == 2:
        fo.seek(0,2)
        name = input("Enter user name : " )
        phone = input("Enter Phone number : ")
        fo.write("Name:")
        fo.write(name)
        fo.write(",Phone:")
        fo.write(phone)
        fo.write("\n")

    elif ch == 3:
        name = input("Enter the name you want to search")
        fo.seek(0,0)
        data = fo.readlines()
        check = 0
        for i in data:
            row = i.split(",")
            n = row[0].split(":")
            if n[1].upper() == name.upper():
                print(row[0] , row[1])
                check = 1
        if check == 0:
            print("\nData Not Found\n")
    elif ch == 4:
        name = input("Enter the name you want to Delete")
        fo.seek(0,0)
        data = fo.readlines()
        fo.close()
        fo2 = open("phone.txt" ,"w")
        check = 0
        for i in data:
            row = i.split(",")
            n = row[0].split(":")
            if n[1].upper() == name.upper():
                check = 1
            else:
                fo2.write(row[0])
                fo2.write(",")
                fo2.write(row[1])
        if check == 0:
            print("\nData Not Found\n")
        else :
            print("\nData Deleted Successfully")
        fo2.close()
        fo = open("phone.txt" , "r+")
    elif ch == 5:
        name = input("Enter the name you want to Delete")
        fo.seek(0,0)
        data = fo.readlines()
        fo.close()
        fo2 = open("phone.txt" ,"w")
        check = 0
        for i in data:
            row = i.split(",")
            n = row[0].split(":")
            if n[1].upper() == name.upper():
                check = 1
                name = input("Enter updataed user name : " )
                phone = input("Enter updated Phone number : ")
                fo2.write("Name:")
                fo2.write(name)
                fo2.write(",Phone:")
                fo2.write(phone)
                fo2.write("\n")
                
            else:
                fo2.write(row[0])
                fo2.write(",")
                fo2.write(row[1])
        if check == 0:
            print("\nData Not Found\n")
        else :
            print("\nData Updated Successfully")
        fo2.close()
        fo = open("phone.txt" , "r+")
    else :
        print("Invalid Input")
