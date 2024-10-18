'''
Author: Ajion Saji
Date : 18/10/2024
Description : a Python program that demonstrates the usage of arithmetic, comparison, and logical operators.
Perform a few operations and print the results.
'''
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
add=(num1+num2)
div=(num1//num2)
print("sum:",add, "division:" ,div,)
print("Is num1 greater than num2 ?:",num1>num2)
print("Are num1 and num2 equal?:",num1==num2)
print("logicalAnd :",num1>0 and num2>0)
print("logicalOr:",num1==num2 or num1>num2)
