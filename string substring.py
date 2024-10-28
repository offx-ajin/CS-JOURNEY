'''
Author: Ajin Saji
Date : 19/10/2024
Description:Create, concatenate, and print a string and access a sub-string from a given string.
'''
string1=input("Enter your first name")
string2=input("Enter your last name")
name=(string1+" "+string2)
print(name)
l=len(string1)
print(l)
last_string=name[l:]
print(last_string)
