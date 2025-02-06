#Day 4. A rock, paper, scissors game with using random module, importing a file and using list
import RPS_ASCII
import random

print(RPS_ASCII.Welcome)
player_choice = int(input("Choose your move. 0 for Rock, 1 for Paper, 2 for Scissors: "))
if(player_choice >= 3):
    print("Wrong number. You disqualified.")
    exit()
print(RPS_ASCII.rps[player_choice])
computer_choice = random.randint(0,2)
print(RPS_ASCII.rps[computer_choice])
if computer_choice == player_choice:
    print(RPS_ASCII.Tie)  
elif computer_choice == 0:
    if player_choice == 1:
        print(RPS_ASCII.Win)
    elif player_choice == 2:
        print(RPS_ASCII.Lose)
elif computer_choice == 1:
    if player_choice == 0:
        print(RPS_ASCII.Lose)
    elif player_choice == 2:
        print(RPS_ASCII.Win)
elif computer_choice == 2:
    if player_choice == 0:
        print(RPS_ASCII.Win)
    elif player_choice == 1:
        print(RPS_ASCII.Lose)        