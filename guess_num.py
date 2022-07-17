from numpy import random
mystery_num = random.randint(1,1001)  # randomly generate a number (reveist this algorithm)
score = 100 # keep track of the users score
print(f"""Are you ready to play the guessing game?

It's simple!

Pick a number from 1 to 1000...

If you guess the Mystery Number and you win!

But! If you guess wrong too many times and you lose!

Your score starts at {score}. Good luck!""")
print()


user_choice = input("Guess a number: ")
while not (user_choice.isdigit() and (int(user_choice) > 1) and (int(user_choice) < 1000)):  # the user's choice 1) must be an integer 2) must be greater than zero 3) must be less than 100
	user_choice = input("You can only enter whole numbers from 1 to 1000\nLet's try again.\n\nGuess a number: ")
	print()
user_choice = int(user_choice)



try_again = False # does the user have another turn
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
clue = ""  # to hold the final clue selected
results = []  # to keep track of each number chosen and the score of the user. The number of turns is the length of the index.
turn = len(results) + 1
clue_list = []
count = 0

i = 2
while i * mystery_num <= (1000):   #create a list of the multiples of the random number 
	multiples_of.append(mystery_num * i)
	i += 1

i = mystery_num - 1
while i > 1: #create a list of the factors of the random number
	if (mystery_num % i == 0):
		factors_of.append(int(mystery_num / i))
	i -= 1


for i in multiples_of: #add the multiples to the list of clues
	clue_list.append({i:"is a multiple of"})
for i in factors_of:   #add the factor to the list of clues
	clue_list.append({i:"is a factor of"})
clue_list.append({str(user_choice):"is greater than"}) if user_choice > mystery_num else clue_list.append({str(user_choice):"is less than"}) #add the last user guess to the list of clues



while True:  
	if user_choice == mystery_num:
		win = True
		break
	else:
		score -= 5

	if score <= 0:
		lose = True
		break

	
	results.append({user_choice: score})

#################################################################################################################
#This will section of code is to create clues for the customer based on their guess
	if len(results) > 0:


		1
		clue_list.pop(-1) #remove the previous user guess from the list of clues
		clue_list.append({str(user_choice):"is greater than"}) if user_choice > mystery_num else clue_list.append({str(user_choice):"is less than"}) #add the last user guess to the list of clues
		
		if len(clue_list) > 1:  # if there is more than one element in clue list ...
			if random.randint(3) > 0:  # select the last element twice as many times as ther other elements
				clue = clue_list[-1]
			else:
				clue = clue_list[random.randint(len(clue_list)) - 1]  # randomly select the other elements
		else: # if there is only one element in clue_list, select that element
			clue = clue_list[0] 
  
########################################################################################################################
	print("Sorry! That isn't the mystery number.")
	print(list(clue.keys())[0], list(clue.values())[0], "the mystery number!")
	print(f"Your score is now {score}!")
	
	user_choice = input("\nPick another number: ")
	
	
	while not (user_choice.isdigit() and (int(user_choice) > 1) and (int(user_choice) < 1000)):
		user_choice = input("You can only enter whole numbers from 1 to 1000\nLet's try again.\n\nGuess a number: ")
		print()
	user_choice = int(user_choice)

		
if win:
	print("\nYou win!")
	print("The Mystery Number is", mystery_num)
	print(f"Your score is {score}!")
	input()
else:
	print("\nYou lose, sorry!")
	print("The Mystery Number is", mystery_num)
	input()