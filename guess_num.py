from numpy import random
import math 

user_choice = int(input("Hello!\n\nPlease enter a number:  "))

mystery_num = math.floor((random.random() * 1000))  # randomly generate a number (reveist this algoritm)
try_again = False # does the user have another turn
score = 100 # keep track of the users score
lose = False # has the looser lost the game yet
win = False # has the user won the game yet
multiples_of = [] # for listing all of the multiples of mystery_num
factors_of = []  # for listing all of the factors of the mystery_num
is_same = False # for checking if the user choice is the same as mystery_num
is_multiple = False  # for checking if user choice is a multiple of mystery_num
is_factor = True  # for checking if user_choice is a factory of myster_num 
user_turn = []  # to track how many times the user has guessed
is_lower = False #  user choice is lower than mystery_num 
is_higer = False #  user choicen is higher than myster_num
clue = ""
results = []
turn = len(results) + 1


while (not win) or (not lose):   
#################################################################################################################
#This will section of code is to create a clue for the customer based on their guess
  while try_again:
    i = 0
    while i * mystery_num <= (1000):
      multiples_of.append(mystery_num * i)
      i += 1
    multiples_of.remove(0)

    i = mystery_num
    while i > 0:
      if mystery_num % i == 0:
        factors_of.append(int(mystery_num / i))
      i -= 1


    if user_choice - mystery_num > 0:
      is_higher = True
      is_lower = False
    else:
      is_higher = False
      is_lower = True

    if user_choice in multiples_of:
      is_multiple = True
    else:
      is_multiple = False

    if user_choice in factors_of:
      is_factor = True
    else:
      is_factor = False

    if is_factor:
      clue = "can be evenly divided by" 
    elif is_multiple:
      clue = "is a multiple of" 
    elif is_higher:
      clue = "is higher than" 
    else: 
      clue = "is lower than" 
# test_list = [{"a": 1}, {"b": 2}, {"c": 3}]
# print(random.choice(test_list))     
#############################################################################################################
  

  if user_choice == mystery_num:
    is_same = True
    win = True
  else:
    is_same = False
    score -= 5
  if score <= 0:
    lose = True
    
  print("Sorry! That wasn't the number\n")
  print(f"{user_choice} {clue} the mystery number!\n")
  user_choice = input("Try picking again: ")  
  results.append({user_choice: score})

  if win or lose:
    try_again = False

if win:
  print("You win!")
  print(f"Your score is {results[len(results) - 1][user_choice]}")
else:
  print("You lose!")

  
