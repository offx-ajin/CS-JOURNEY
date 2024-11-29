def triangle():
    l1=[]
    s1=int(input("Enter the first side:"))
    l1.append(s1)
    s2=int(input("Enter the second side:"))
    l1.append(s2)
    s3=int(input("Enter the third side:"))
    l1.append(s3)
    l1.sort()
    if l1[2]**2==l1[1]**2 + l1[0]**2:
        print("its a right angled triangle ")
    else:
        print("its not a right angled triangle")

triangle()
