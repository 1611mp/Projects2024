"""Rock - Paper - Scissor Project"""
import random
comp_score = 0
player_score = 0
user_wish = input("Do you wish to play game. y or n?").lower().strip()
if user_wish == "y":
    
    while comp_score < 5 and player_score < 5:
        my_choice = input("Please enter your choice rock, paper or scissor: ").capitalize()
        comp_choice = random.choice(['Rock', 'Paper', 'Scissor'])

        print("The computer has chosen {}.".format(comp_choice))

        if my_choice == "Rock" and comp_choice == "Paper":
            print("Paper beats Rock")
            comp_score += 1
            print(f"Computer score : {comp_score}.")
        elif my_choice == "Rock" and comp_choice == "Scissor":
            print("Rock beats Scissor")
            player_score += 1
            print(f"Player score : {player_score}.")
        elif my_choice == "Scissor" and comp_choice == "Paper":
            print("Scissor cuts Paper")
            player_score += 1
            print(f"Player score : {player_score}.")
        elif my_choice == "Scissor" and comp_choice == "Rock":
            print("Rock beats Scissor")
            comp_score += 1
            print(f"Computer score : {comp_score}.")
        elif my_choice == "Paper" and comp_choice == "Scissor":
            print("Scissor cuts Paper")
            comp_score += 1
            print(f"Computer score : {comp_score}.")
        elif my_choice == "Paper" and comp_choice == "Rock":
            print("Paper beats Rock")
            player_score +=1
            print(f"Player score : {player_score}.")


    
print(f"The final score is Player Score: {player_score}, Computer Score: {comp_score}.")
