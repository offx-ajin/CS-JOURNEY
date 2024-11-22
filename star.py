

row = int(input(" enter the rows"))

for i in range (1,row+1):
    for j in range (i):
        print ("*"*1 ,end= "\t")
    print()




row =int(input("enter the rows:"))
for i in range (row,0,-1):
    for j in range (1):
        print ("*"*i ,end="\t")
    print()


print("Hill Pattern")
row=int(input("enter no of rows"))
for i in range (1,row+1):
    for j in range(row-i):
        print(' ',end='')
    for k in range (2*i-1):
        print("*", end='')
    print()

limit=int(input("enter the number the rows"))
for i in range (limit+1,0,-1):
    for j in range (limit-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()