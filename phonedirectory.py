def createInfo():
    name = input("Enter user name : " )
    phone = input("Enter Phone number : ")

    fo = open("phone.txt" , "a")

    fo.write("Name:")
    fo.write(name)
    fo.write(",Phone:")
    fo.write(phone)
    fo.write("\n")

    fo.close()

def readInfo():
    fo = open("phone.txt" , "r")
    #read() -> reads all the data in str format
    #readline() -> reads only the first row in str format
    #readlines() -> read the data line by line in list format
    data = fo.readlines()
    print(data)

    fo.close()
    

#createInfo()
readInfo()
