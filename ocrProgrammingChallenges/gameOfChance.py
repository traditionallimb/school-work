from random import *


def main_menu():
	menuLoopCtrl = 1
	print("\n\n==========GAME OF CHANCE==========")
	print("\n\t1. Play a Round\n\t2. View Cash Pot\n\t3. Rules\n\t4. Save and Exit")

	while menuLoopCtrl == 1:
		menuLoopCtrl = 2
		userChoice = int(input("\nEnter a number > "))
		errorCheck = [userChoice >= 1, userChoice <= 4, type(userChoice) == int]
		if all(errorCheck):
			menuLoopCtrl = 3
		else:
			print("That isn't a valid input, please try again.")
			menuLoopCtrl = 1
	return userChoice


def play_round():
	def isPrime(N):
		for number in range(2, N):
			if N % number == 0:
				return False
		return True
	betLoopCtrl = 1
	userCashPot = 10
	print(f"You currently have {userCashPot} tokens to play with.")
	while betLoopCtrl == 1:
		betLoopCtrl = 2
		userBet = int(input("What number between 0-30 would you like to bet on? > "))
		errorCheck = [userBet >= 0, userBet <= 30, type(userBet) == int]
		if all(errorCheck):
			confirm = str(input(f"The number you are betting on is: {userBet}.\nWould you like to change this? [y,n] > "))
			if confirm == 'y': betLoopCtrl = 1
			else: betLoopCtrl = 3
		else:
			print("That isn't a valid input, please try again.")
			betLoopCtrl = 1

	betAmountLoopCtrl = 1
	while betAmountLoopCtrl == 1:
		betAmountLoopCtrl = 2
		userBetAmount = int(input(f"How much would you like to bet? > "))
		errorCheck = [userBetAmount <= userCashPot, userBetAmount > 0, type(userBetAmount) == int]
		if all(errorCheck):
			confirm = str(input(f"The number you are betting on is: {userBetAmount}.\nWould you like to change this? [y,n] > "))
			if confirm == 'y': betAmountLoopCtrl = 1
			else: betAmountLoopCtrl = 3
		else:
			print("That isn't a valid input, please try again.")
			betAmountLoopCtrl = 1


	numGen = randint(0, 30)
	multiplier = 1
	print(f"The actual number is: {numGen}")
	if numGen % 2 == 0:
		print("This is an even number, so your bet will be doubled if you guessed right!")
		multiplier *= 2
	if numGen % 10 == 0:
		print("This is a multiple of 10, so your bet will be tripled if you guessed right!")
		multiplier *= 3
	if isPrime(numGen):
		print("This is a prime number, so your bet will be quintupled if you guessed right!")
		multiplier *= 5
	if numGen < 5:
		print("This is a very small number, so your bet will be doubled if you guessed right!")
		multiplier *= 2

	print(f"You guessed: {userBet}")
	if userBet == numGen:
		print("YOU WIN!!!")
		print(f"{userBetAmount * multiplier} will be added to your total winnings")
		userWinnings = (userBetAmount * multiplier) - userBetAmount
	elif userBet != numGen:
		print("You lost :(")
		print(f"{userBetAmount} will be removed from your total winnings")
		userWinnings = userBetAmount


	# The plan is to limit the number of tokens that can be bet each round to 10



loopCtrl = 1
while loopCtrl == 1:
	loopCtrl = 2
	menuChoice = main_menu()
	if menuChoice == 1:
		play_round()
		loopCtrl = 1
	elif menuChoice == 2:
		view_cash()
		loopCtrl = 1
	elif menuChoice == 3:
		rules()
		loopCtrl = 1
	elif menuChoice == 4:
		save()
