'''
Author : Ajin Saji
Date : 28/1024
Description:a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit.
The program should repeatedly display a menu with three options
'''
while True:
    print("1.\tconvert celsius to fahrenheit")
    print("2.\tconvert fahreheit to celsius")
    print("3.\texit the program")
    choice=int(input("enter yout choice:"))
    if choice ==1:
       temp=float(input("enter the temperature:"))
       temp_in_F=(temp*9/5)+32
       print(f" the temperature in fahrenheit :{temp_in_F}")
    elif choice ==2:
        temp = float(input("enter the temperature:"))
        temp_in_C=(temp-32)*5/9
        print(f" the temperature in celsius:{temp_in_C}")
    elif choice ==3:
        exit()
    else:
        print("invalid choice")