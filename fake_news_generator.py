import random

subjects = [
  "messi",
  "ronaldo",
  "neymar",
  "mbappe",
  "ishowspeed",
  "monkey d luffy",
  "naruto uzumaki",
]

actions = [
  "love you",
  "eat your homework",
  "fight at the",
  "dance",
  "play cricket at parliment",
  "play football",
  "eat banana"
]

places_or_things = [
  "at the white house",
  "at the moon",
  "at the park",
  "at house",
  "during the match",
  "in the jungle",
  "at school",
  "in underwater city"
]

while True:
  subject = random.choice(subjects)
  action = random.choice(actions)
  place_or_thing = random.choice(places_or_things)

  fake_news = (f"Breaking News: {subject.capitalize()} {action} {place_or_thing}!")
  print("\n"+fake_news)

  user_input = input("\nDo you want to generate another fake news? (Y/N): ").strip().lower()
  if user_input == 'n':
   break

  # Goodbye message
print("Thank you for using the Fake News Generator. Goodbye!")