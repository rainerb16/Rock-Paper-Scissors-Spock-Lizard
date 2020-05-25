#Rock Paper Scissors Spock Lizard
from random import randint

# Create a list of play options
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

play = True

while play == True:

    #Ask player to select option
    computer = t[randint(0, 4)]
    user_input = input("Please select: Rock, Paper, Scissors, Spock or Lizard\n")
    u = user_input.lower()

    player = u.capitalize()

    print("Player: ", player)
    print("Computer: ", computer)

    #If result is tie
    if player == computer:
        print("Tie!")

    #If Player selects Rock
    elif player =="Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You win!", player, "crushes", computer)
        elif computer == "Spock":
            print("You lose!", computer, "vaporizes", player)


    #If player selects Paper
    elif player =="Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        elif computer =="Rock":
            print("You win!", player, "covers", computer)
        elif computer == "Lizard":
            print("You lose!", computer , "eats", player)
        elif computer == "Spock":
            print("You win!", player, "disproves", computer)

    #If player selects Scissors
    elif player == "Scissors":
        if computer == "Paper":
            print("You win!", player, "cuts", computer)
        elif computer == "Rock":
            print("You lose!", computer, "crushes", player)
        elif computer =="Lizard":
            print("You win!", player, "decapitates", computer)
        elif computer == "Spock":
            print("You lose!", computer, "smashes", player)

    #If player selects Lizard
    elif player == "Lizard":
        if computer =="Rock":
            print("You lose!", computer, "crushes", player)
        elif computer =="Paper":
            print("You win!", player, "eats", computer)
        elif computer == "Scissors":
            print("You lose!", computer, "decapitates", player)
        elif computer == "Spock":
            print("You win!", player, "", computer)

    #If player selects Spock
    elif player == "Spock":
        if computer == "Rock":
            print("You win!", player, "vaporizes", computer)
        elif computer == "Paper":
            print("You lose!", computer, "disproves", player)
        elif computer == "Scissors":
            print("You win!", player, "smashes", computer)
        elif computer == "Lizard":
            print("You lose!", computer, "poisons", player)


    print("Would you like to play again? \n")
    answer =input()

    if answer.lower() =="y" or answer.lower() =="yes":
        play == True
    else:
        break
