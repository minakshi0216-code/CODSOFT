# created by Minakshi
import random

def play_round():
    print("\n--- Rock Paper Scissors Game ---")
    print("Choices: rock / paper / scissors")

    user = input("Enter your choice: ").lower()
    choices = ["rock", "paper", "scissors"]

    if user not in choices:
        print(" Invalid ")
        return play_round()  

    computer = random.choice(choices)
    print(f"\nComputer chose: {computer}")

    if user == computer:
        print("tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win")
    else:
        print("Computer wins")

    play_again()  


def play_again():
    again = input("\nWanna play again? (yes/no): ").lower()
    if again == "yes":
        play_round()
    elif again == "no":
        print("\nThanks for playing ")
    else:
        print("Type yes or no only")
        play_again()  



play_round()