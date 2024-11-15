import random
list1=['rock','paper','scissor']
while True:

    my_choice=input("enter your choice:")
    computer_choice = random.choice(list1)
    print('computer choice is :', computer_choice)
    if my_choice==computer_choice:
        print("its a tie")
    elif my_choice =='rock':
        if computer_choice == 'paper':
            print("you lose")
        else:
            print("you win")
    elif my_choice =='scissor':
        if computer_choice == 'rock':
            print("you lose")
        else:
            print("you win")
    elif my_choice =='paper':
        if computer_choice == 'scissor':
            print("you lose")
        else:
            print("you win")








