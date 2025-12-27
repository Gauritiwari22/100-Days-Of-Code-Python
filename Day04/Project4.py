import random
print("ROCK-PAPER-SCISSORS")

rock=  ''' _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper=''' _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor='''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_images=[rock,paper,scissor]

user_choice=int(input("What do you choose? Type 0 for ROCK, 1 for PAPER and 2 for SCISSORS:"))
if user_choice >= 3 or user_choice < 0:
    print("INVALID CHOICE")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:{computer_choice}")
    print(game_images[computer_choice])
    if computer_choice==user_choice:
        print("TIE")
    elif computer_choice==2 and user_choice==0:
        print("YOU WIN!")
    elif computer_choice==0 and user_choice==2:
        print("COMPUTER WINS!")
    elif user_choice>computer_choice:
        print("YOU WIN!")
    elif user_choice<computer_choice:
        print("COMPUTER WINS!")
