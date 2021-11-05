import random

x=random.randint(1,25)
trying=0
while True:
    guess=int(input("Guess a random number between 1-25! "))
    if x==guess:
        trying+=1
        print(f"Congrulations! You did it on {trying} times!")
        break
    elif x<guess:
        print("Decrease your number!") 
        trying+=1
    else:
        print("increase your number!")
        trying+=1
    