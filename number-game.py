import random

playing= True
number= str(random.randint(0,9))

print("I will generate a number 0,9 ,Youhave to guess the number one digit at a time")

print("The game ends when you guess the right number")

while playing:
    guess=input("Give me your best guess\n")

    if number== guess:
        print("You win the game!")
        print("The number was",number)
        break
    else:
        print("Looks like you lost the game!,Try again later")