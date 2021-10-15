import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
 '''

print("\nWelcome to Rock Paper Scissors!\n")


# player_list = [rock,]
# computer_list =
choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type:\n0 for Rock\n1 for Paper\n2 for Scissors\n\nChoice: "))
computer_choice = random.randint(0, 2)

if 0 <= player_choice <= 2:                             # catches invalid player choice
    print(f"\nPlayer: \n{choices[player_choice]}")
    print(f"Computer: \n{choices[computer_choice]}")

    if player_choice == computer_choice:
        print("\n\nIt's a draw. Please try again!")
    elif player_choice == 0 and computer_choice == 1:
        print("\n\nYou LOSE!")
    elif player_choice == 0 and computer_choice == 2:
        print("\n\nYou WIN!")
    elif player_choice == 1 and computer_choice == 0:
        print("\n\nYou WIN!")
    elif player_choice == 1 and computer_choice == 2:
        print("\n\nYou LOSE!")
    elif player_choice == 2 and computer_choice == 0:
        print("\n\nYou LOSE!")
    elif player_choice == 2 and computer_choice == 1:
        print("\n\nYou WIN!")
else:
    print("You chose an invalid number")


