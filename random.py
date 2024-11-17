import random
num=random.randint(0,5)
#print(num)

playing=True
while playing:
    guess=int(input("Please enter number from 0 to 5"))
    if num==guess:
        print("You win the game!")
        break
    else:
        print("You lose!")