import random
playing = True
options = ["Rock", "Paper", "Scissors"]
while playing == True:

    userchoice = input("Enter Rock, Paper, or Scissors: ")

    computerchoice = random.choice(options)
    print("You chose:", userchoice)
    print("Computer chose:", computerchoice)

    if userchoice == computerchoice:
        print("It's a tie!")
    elif userchoice == "Rock" and computerchoice == "Scissors":
        print("Rock beats scissors! You win!")
    elif userchoice == "Paper" and computerchoice == "Rock":
        print("Paper beats Rock! You win!")
    elif userchoice == "Scissors" and computerchoice == "Paper":
        print("Scissors beats Paper! You win!")
    else:
        print(computerchoice ,"beats", userchoice, "! You lose!")