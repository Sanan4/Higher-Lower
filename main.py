import random
import art as art
import game_data as d

# Score
score = 0

# Logo
print(art.logo)

# Asking user if they want to play
want_to_play = input("Do you want to play a game? Type 'y' or 'n': ")
if want_to_play == "y":
    want_to_play = True
else:
  want_to_play = False

dict_b = random.choice(d.data)


# Game
while want_to_play:

  # Rules
  print("\nThe rules are simple, you have to pick between two people and guess which one has the higest instagram followers. If you fail it's game over. If you win you get a point and continue.\n")
  
  # Displays option A
  dict_a = dict_b
  a = dict_a['follower_count']
  person_a = dict_a['name']
  description_a = dict_a['description']
  country_a = dict_a['country']
  print('Compare A: ' + person_a + ", a " + description_a + ', from ' + country_a + '\n')
  print(art.vs)
  
  dict_b = random.choice(d.data)
  b = dict_b['follower_count']

  # Checks if A and B are the same and changes it
  if dict_a == dict_b:
    dict_b = random.choice(d.data)
    
  # Displays option A
  person_b = dict_b['name']
  description_b = dict_b['description']
  country_b = dict_b['country']
  print('Compare B: ' + person_b + ", a " + description_b + ', from ' + country_b + '\n')
  
  # Asks user to pick A or B
  input_a = input("Who has more followers? Type 'A' or 'B': \n")
  input_a = input_a.lower()

  if input_a == 'a':
    if a > b:
      print("You are correct! \n")
      score += 1
      
    else:
      print(f"Sorry, the correct answer is {person_b}. \n", "Game Over")
      want_to_play = False
      
  elif input_a == 'b':
    if b > a:
      print("You are correct! \n")
      score += 1
      person_b = person_a
      description_b = description_a
      country_b = country_a
      
    else:
      print(f"Sorry, the correct answer is {person_a}. \n", "Game Over")
      want_to_play = False
    
  # Asks user if they want to continue playing
  if want_to_play == False:
    print(f"Your final score is {score}.")
    break
