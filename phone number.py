'''
Author : Ajin Saji
date : 29/11/24
Description :Program to check whether the given number
is a valid mobile number or not using functions.
'''
def num():
    n=input("Enter your phone number:")
    a=str(n)
    if len(a)==10 and n[0] in ["7","8","9"]:
        return "The given number is valid "
    return "the given number is invalid"
print(num())