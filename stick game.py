print("Welcome to Stick Game ")

def stick_game():
    p1= input("Enter the name of the player: ")
    p2= input("Enter the name of the player: ")
    sticks = 16
    while sticks>0:
        s1=int(input(f"{p1}, chose 1,2,3 sticks: "))
        if s1>3 or s1<1:
            print("Invalid stick Game over")
            break
        sticks = sticks - s1
        print(f"number of sticks remaining ={sticks}")
        if sticks<=0:
            print(f"{p1} lost. better luck next time")
            print(f"{p2} you won congratulations")
            break
        s2=int(input(f"{p2}, chose 1,2,3 sticks: "))
        if s2>3 or s2<1:
            print("invalid input game over ")
            break
        sticks= sticks - s2
        print(f"number of sticks remaining ={sticks}")
        if sticks<=0:
            print(f"{p2} lost. Better luck next time")
            print(f"\n{p1} you won. Congratulations")
            break
print(stick_game())

