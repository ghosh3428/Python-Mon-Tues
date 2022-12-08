#open("name" , "mode")

fo = open("niit.txt" , "w")

print("Niit.txt opened in read mode")

data = "Hello my name is Niit Jadavpur."
#write(str)
print("Writing data to the file")
fo.write(data)

fo.write("\n123\n")


name =["Amit" , "Sumit" , "Ajay" ,"Vijay"]

fo.writelines(name )

fo.close()
print("Niit.txt closed")
