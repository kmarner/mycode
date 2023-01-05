#!/usr/bin/env python3
"""Rock Paper Scissors Game | by Keriise Griffin-Marner"""

import random

# user needs to make a choice
# random module
# computer needs to make a choice
# choices need to be evaluated (winner)
# print result (who won)

def main():
    """body of the game"""
    
    choice= input("Rock, Paper, or Scissors?\n>")
    botchoice= random.choice(["rock", "paper", "scissors"])

    choice= choice.lower() # validates input by forcing input to be lower case

    # uncomment these print functions to debug
    #print(choice)
    #print(botchoice)

    if choice not in ["rock", "paper", "scissors"]:
        print("You entered an invalid choice, you lose(r)!")

    elif choice == "scissors" and botchoice == "paper":
        print("You win!")

    elif choice == "scissors" and botchoice == "rock":
        print("Better luck next time!") 

    elif choice == "scissors" and botchoice == "scissors":
        print("It's a tie!")


    elif choice == "rock" and botchoice == "scissors":
        print("You win!")

    elif choice == "rock" and botchoice == "paper":
        print("Better luck next time!")

    elif choice == "rock" and botchoice == "rock":
        print("It's a tie!")  

    elif choice == "paper" and botchoice == "rock":
        print("You win!")

    elif choice == "paper" and botchoice == "scissors":
        print("Better luck next time!")
  
    elif choice == "paper" and botchoice == "paper":
        print("It's a tie!")    
    # user picked scissors... did they win or lose?

    ### ADD MORE HERE

main()
