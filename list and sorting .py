'''
Author : Ajin Saji
'''



list1=[]
n=int(input("enter the digits"))
for i in range (n):
    num=int(input("enter the number:"))
    list1.append(num)
list2=[]
x=int(input("enter the digits:"))
for i in range (x):
    y=int(input("enter the numbers:"))
    list2.append(y)
list3=list1+list2
even_list=[]
odd_list=[]
for i in list3:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
    even_list.sort()
    odd_list.sort()
list4=even_list+odd_list
print(list4)
