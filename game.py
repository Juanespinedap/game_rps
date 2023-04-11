import random
from os import system

system("cls")  # clean console in windows system

# list of in-game tools
kit = ['rock', 'paper', 'scissors']

print(f"\n Welcome to the game \n")

# function to run the game
def game():

    victories = 0
    defeats = 0

    while (victories < 3) and (defeats < 3):

        print("-----------------------------------")
        choice = input("\n Choose between \n - Rock or R \n - Paper or P \n - Scissors or S \n").lower()
            
        # user choice and value assignment
        if (choice == 'rock') or (choice == 'r'):
            player = 'rock'
        elif (choice == 'paper') or (choice == 'p'):
            player = 'paper'
        elif (choice == 'scissors') or (choice == 's'):
            player = 'scissors'
        else:
            # input correction
            system("cls") 
            print("\n You chose something different from the options \n Try again! \n")
            print(f"You have {victories} wins and {defeats} losses \n")
            continue

        # show the user's choice
        print("\n You choose: " + player.capitalize())

        # random method for pc
        pc = random.choice(kit)
        # show the pc's choice
        print(" Pc choose: " + pc.capitalize(), "\n")
        print("That means....")
        
        # logic system game
        if player == pc:
            print("Both are fucking assholes")
            print(f"\n You have {victories} wins and {defeats} losses")
        elif (player == "rock" and pc == "scissors") or (player == "paper" and pc == "rock") or (player == "scissors" and pc == "paper"):
            print("You're a fucking winner")
            victories +=1
            print(f"\n You have {victories} wins and {defeats} losses")
        else:
            print("You're a fucking loser")
            defeats +=1
            print(f"\n You have {victories} wins and {defeats} losses")

    print("-----------------------------------\n")
    print(f"The final result: {victories} wins and {defeats} losses")

    if victories > defeats:
        print("\n You are the winner. Congratulations!! \n")
    elif victories < defeats:
        print("\n I'm sorry, the winner is the PC. Good luck the next time!! \n")
    
    keep_going()


# function to continue game
def keep_going():

    # ask the user if they want to continue playing
    question = input(f"Do you want to keep playing? yes or no (y/n) \n: ").lower()

    # user response
    if (question == "yes") or (question == "y"):
        system("cls")
        game()
    else:
        print("Good game, see you soon!!  \n")
        exit()


if __name__ == '__main__':
  game()
  keep_going()