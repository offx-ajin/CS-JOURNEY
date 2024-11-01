'''
Author :Ajin Saji
Date : 18/10/2024
Description :a Python program that uses functions from the math module to perform the following operations on a number provided by the user:

    Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.'''
import math
num1= int(input("enter a number "))
square_root=math.sqrt(num1)
print("square root of ",num1,":" ,square_root)
print("factorial of ",num1, ":" ,math.factorial (num1))
print("raise to power 2",num1, ":" ,math.pow (num1, 2))
