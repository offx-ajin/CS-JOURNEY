'''
Author Ajin Saji
Date : 25/10/2024
Description:a Python program to convert temperature values back and forth between Celsius and Fahrenheit
'''
temp=float(input("enter the temperature:"))
unit=input("(C)elcius or (F)ahrenheit ?:")
if unit=="C":
    fahrenheit=(9/5*temp)+32
    print("celsius to fahrenheit:",fahrenheit)
else:
    celsius=5/9*(temp-32)
    print("fahrenheit to celsius:",celsius)
