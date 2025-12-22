import random 

easy_words = ['cat', 'dog', 'fish', 'bird', 'tree']
medium_words = ['python', 'jumble', 'dolphin', 'guitar', 'puzzle']
hard_words = ['elephant', 'giraffe', 'alligator', 'hippopotamus', 'chimpanzee'] 

print("Welcome to the Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter the difficulty level: ").lower().strip()

if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print("Invalid difficulty level. Defaulting to easy.")
    secret = random.choice(easy_words)

attemts = 0
print("\nGuess the word!")

while True:
    guess = input("Enter your guess:").lower().strip()
    attemts += 1

    if guess == secret:
        print(f"Congratulations! You've guessed the word '{secret}' in {attemts} attempts.")
        break
    
    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print(f"Hint: {hint}")
    print("Try again!\n")
    

