from numpy import random
import math 


mystery_num = math.floor((random.random() * 1000))  # randomly generate a number
try_again = True # does the user have another turn
score = 100 # keep track of the users score
lose = False # has the looser lost the game yet
win = False # has the user won the game yet
user_choice = 0  # to hold the users guess
multiples_of = [] # for listing all of the multiples of mystery_num
factors_of = []  # for listing all of the factors of the mystery_num
is_same = False # for checking if the user choice is the same as mystery_num
is_multiple = False  # for checking if user choice is a multiple of mystery_num
is_factor = True  # for checking if user_choice is a factory of myster_num 
user_turn = []  # to track how many times the user has guessed
is_higher = False # is mystery_num higher than the user choice
is_lower = False # is mystery_num lower than the user choic

#################################################################################################################
#This will section of code is to create a clue for the customer based on their guess
i = 0
while i * mystery_num <= (1000):
  multiples_of.append(mystery_num * i)
  i += 1





if mystery_num == user_choice:
  is_same = True
elif user_choice - mystery_num < 0:
  is_higher = True
  is_lower = False
else:
  is_higher = False
  is_lower = True

    

while try_again == True:
  if len(user_turn) > 0:
    #run the clue function here
    print()
  user_choice = input("Please enter a number: ")



# test_list = [{"a": 1}, {"b": 2}, {"c": 3}]
# print(random.choice(test_list))
