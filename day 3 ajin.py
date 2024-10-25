'''
Author:AjinSaji
Date : 25/10/2024
Description : a Python program to find
the largest of three numbers
'''
num1=int(input("enter the number 1:"))
num2=int(input("enter the number2:"))
num3=int(input("ente the number 3:"))
if num1>num2 and num1>num3:
    print("number 1 is greater")
elif num2>num1 and num2>num3:
    print("number 2 is greater")
else:
    print("number 3 is greater")

