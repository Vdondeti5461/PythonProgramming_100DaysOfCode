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
---'   ____)____
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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 0 for Rock , 1 for Paper or 2 for Scissors.\n"))
if user_choice >=3 or user_choice < 0:
    print("You typed a invalid number , You lose")
else:
    print(game_images[user_choice])

    Computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[Computer_choice])


    if user_choice == 0 and Computer_choice == 2:
        print("You Win!")
    elif Computer_choice == 0 and user_choice ==2:
        print("You Lose")
    elif Computer_choice > user_choice:
        print("You Lose")
    elif user_choice > Computer_choice:
        print("You Win")
    elif Computer_choice == user_choice:
        print("It's a draw")
