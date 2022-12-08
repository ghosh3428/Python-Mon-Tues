#1
#12
#123
#1234
#12345

for i in range(2,7,1):
    for j in range(1,i,1):
        print(j , end='')
    print()   

#1
#21
#321
#4321
#54321
for i in range(1,6,1):
    for j in range(i ,0,-1):
        print(j , end="")
    print()

#5
#45
#345
#2345
#12345
for i in range(5,0,-1):
    for j in range(i ,6,1):
        print(j , end="")
    print()

#N
#NI
#NII
#NIIT
name = "NIIT"
for i in range(1,5,1):
    for j in range(0 ,i,1):
        print(name[j] , end="")
    print()
#1
#2  3
#4  5  6
#7  8  9  10
#11 12 13 14 15
c= 1
for i in range(2,7,1):
    for j in range(1,i,1):
        print(c, end=' ')
        c = c+1
    print() 

#    1
#   12
#  123
# 1234
#12345

for i in range(2,7,1):
    for s in range(1,7-i,1):
        print(' ' , end="")
    for j in range(1,i,1):
        print(j , end='')
    print() 