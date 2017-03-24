import sys
import os
import random

'''Randomly picks a number from a set range dependent on the difficulty chosen and compares it to user input.
Then outputs if the user guessed right or wrong and what percentage were they off by'''

#FUNCTIONS--------------------------------------------------------------------#

def deviation(true_val,guess_val):	#calculates the deviated percentage

	diff = guess_val - true_val

	if diff < 0:

		diff = diff / -1

	return (diff/true_val) * 100

def guess_A_num(random_number, user_pick):	#compares user and computer numbers and prints an output on the screen

	accuracy = random_number - user_pick

	acc_percent = deviation(random_number,user_pick)	#Deviation function call

	if accuracy == 0:

		print ("\nARE YOU A MIND-READER?!!!.....I only ask because u were so DEAD ON!!!")

	if accuracy > 0:

		print ("\nWhoops! Sorry your guess was a little too HIGH\n")

		print ("\nYour were off by about %.2f percent\n" %(acc_percent))

	if accuracy < 0:

		print ("\nWhoops! Sorry your guess was a little too LOW\n")

		print ("\nYour were off by about %.2f percent" %(acc_percent))

#*******************************************************************************

print ("***********WELCOME TO GUESS THE NUMBER GAME*************")

print ("READY TO PLAY?\n")

ans = "Yes"

while (ans != "No"):
	
	while True:		#Loop used to validate input

		response =  input("\nType Yes or No: ").strip() 	#Ensure that input always fall within validation loops

		if response == "Yes":

			while True:

				print ("\nDifficulty levels to play:\n")

				print ("1---Easy\n")

				print ("2---Medium\n")

				print ("3---Hard\n")

				difficulty = int(input("Pick a difficulty: "))


				if difficulty == 1:

					random_number = random.randrange(1,10)		#Using random class this function randrange can spit out any number inclusive of the specified range

					break		#Ensure to break the loop whenever the input passes the validation

				elif difficulty == 2:

					random_number = random.randrange(1,50)

					break

				elif difficulty == 3:

					random_number = random.randrange(1,100)

					break

				else:

					print("\nSorry that choice does not exist. \n\nPlease choose a number from the list.\n")

					continue 	#Allows the loop to start over

			user_pick = int(input("Lets see how a good guesser you are :D\n\nGUESS A NUMBER: "))

			guess_A_num(random_number,user_pick) 	#Call for the guess a number function defined above

			print ("\nWould you like to play again? Dont FORGET practice is KEY! :D LOL\n")

			ans = input("Type Yes or No: ").strip()

			break

		elif response == "No":
			
			print ("\nNo problem, PLEASE COME BACK and PLAY :D\n")
			
			ans = "No"

			break

		else:

			print("\nSorry, but that input does not exist\n")

			print("Please choose again")

print ("\nNext Time Then :D")



