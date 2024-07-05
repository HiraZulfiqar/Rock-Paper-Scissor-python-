import random
options = ["rock", "scissor", "paper"]

user_choice = input("chose rock, paper, or scissor: ")
computer_choice = random.choice(options)

print("your chose:", user_choice)
print( "computer chose:", computer_choice)

if user_choice == computer_choice:
    print("it's a tie!")
elif user_choice == "rock" and computer_choice == "scissor":
    print("you win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("you win!")
elif user_choice == "scissor" and computer_choice =="paper":
    print("you win!")
else:
    print("computer wins!")

