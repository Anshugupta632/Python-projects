import random

choices = ['r', 'p', 's']
while True:
    user_choice = input("Rock, Paper, or Scissors? (R/P/S): ").lower()
    if user_choice not in choices:
        print("Invalid input. Please enter R, P, or S.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice.upper()}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == 'r' and computer_choice == 's') or 
         (user_choice == 'p' and computer_choice == 'r') or 
         (user_choice == 's' and computer_choice == 'p')):    
        print("You win!")
    else:
        print("Computer wins!")

    should_continue = input("Do you want to play again? (Y/N): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break