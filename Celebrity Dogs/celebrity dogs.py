# the value i have been using for testing is 6, so if comments reference 6 or 3, then that is why
import time
import sys
import random as rand
import numpy as np


def menu():
    # loading animation

    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    # menu system

    print("\rWelcome to Celebrity Dogs Top Trumps!")
    loopCtrl = 1
    while loopCtrl == 1:
        loopCtrl = 2
        usrOp = int(input("Please choose a number:\n\t1. Play Game\n\t2. Quit\n> "))
        if usrOp == 1:
            return True
        elif usrOp == 2:
            print("Thank you for playing Celebrity Dogs Top Trumps!")
            time.sleep(2)
            loopCtrl = 3


def setup():
    numberOfCards = int(input("How many cards would you like to play with? The number has to be between 4 and 30, "
                              "and must be even:\n> "))
    if numberOfCards % 2 == 0 and 4 <= numberOfCards <= 30:
        with open("dogs.txt", "r") as dogList:
            # reads files to array
            dogList = dogList.read().splitlines()
            dogList = [line.split(",") for line in dogList]

            # two variables to handle the change in cards - win con
            playerNoOfCards = int(numberOfCards / 2)
            computerNoOfCards = int(numberOfCards / 2)

            # picks random cards from big dog list (picked by half the number of cards the player specified) to list
            playerCardList = np.array([rand.sample(dogList, k=playerNoOfCards)])  # i had to make it a numpy array to be able to more easily deal with it, since it became a 3d array
            playerCardList = playerCardList.flatten().tolist()  # this squishes the 3d array to a 1d array and then makes it a normal python array

            computerCardList = np.array([rand.sample(dogList, k=computerNoOfCards)])
            computerCardList = computerCardList.flatten().tolist()
            for i in range(len(computerCardList)):
                if i in playerCardList:
                    print(i)
                    computerCardList.remove(i)
                    computerCardList.append(rand.sample(dogList, k=1))

            # print(f"Player Cards: {playerCardList}\nComputer Cards: {computerCardList}")  # DEBUG LINE
            playerStatList = []
            computerStatList = []

            # this loop should create a list that has dictionaries with all the values of the dogs picked above
            for i in range(int(numberOfCards/2)):
                playerCurrentCard = rand.choice(playerCardList)
                computerCurrentCard = rand.choice(computerCardList)
                playerCurrentCard = str(playerCurrentCard).strip(",[']")
                computerCurrentCard = str(computerCurrentCard).strip(",[']")
                # print(f"computerCurrentCard variable value: {computerCurrentCard}\t - Should be one value")  # DEBUG LINE

                # creates a dictionary with the players current card and then writes it to a list and then deletes
                # the dog it has the value for
                playerCurrentCardStats = {
                    "name": playerCurrentCard,
                    "exercise": rand.randint(1, 5),
                    "intelligence": rand.randint(1, 100),
                    "friendliness": rand.randint(1, 10),
                    "drool": rand.randint(1, 10)  # lower == better
                }

                computerCurrentCardStats = {
                    "name": computerCurrentCard,
                    "exercise": rand.randint(1, 5),
                    "intelligence": rand.randint(1, 100),
                    "friendliness": rand.randint(1, 10),
                    "drool": rand.randint(1, 10)  # lower == better
                }

                playerStatList.append(playerCurrentCardStats)
                computerStatList.append(computerCurrentCardStats)
                # print(playerStatList)
                playerCardList.remove(str(playerCurrentCard))
                computerCardList.remove(str(computerCurrentCard))
                # print(f"The Card Stats: {playerCurrentCardStats}\nThe list of Dog Stats: {playerStatList}\nThe updated PlayerCardList: {playerCardList}")

            return numberOfCards, playerNoOfCards, playerStatList, computerNoOfCards, computerStatList


def gameplay(numberOfCards, playerNoOfCards, playerStatList, computerNoOfCards, computerStatList):
    loopCtrl = 1
    winner = "player"
    while loopCtrl == 1:
        playerCurrentCardStats = rand.choice(playerStatList)
        computerCurrentCardStats = rand.choice(computerStatList)
        print(f"\n\nYour Card:\nName: {playerCurrentCardStats['name']}\nExercise: {playerCurrentCardStats['exercise']}\nIntelligence: {playerCurrentCardStats['intelligence']}"
              f"\nFriendliness: {playerCurrentCardStats['friendliness']}\nDrool: {playerCurrentCardStats['drool']}")
        if winner == "player": category = int(input("\nWhich category would you like to pick:\n\t1. Exercise\n\t2. Intelligence\n\t3. Friendliness\n\t4. Drool"))
        elif winner == "computer": category = rand.randint(1, 4)
        if category == 1:
            if int(playerCurrentCardStats['exercise']) >= int(computerCurrentCardStats['exercise']):
                print("\nYOU WON!!")
                playerNoOfCards += 1
                computerNoOfCards -= 1
                computerStatList.remove(computerCurrentCardStats)
                playerStatList.append(computerCurrentCardStats)
                winner = "player"
            elif playerCurrentCardStats['exercise'] < computerCurrentCardStats['exercise']:
                print("\nYOU LOST!!")
                playerNoOfCards -= 1
                computerNoOfCards += 1
                computerStatList.append(playerCurrentCardStats)
                playerStatList.remove(playerCurrentCardStats)
                winner = "computer"
        elif category == 2:
            if playerCurrentCardStats["intelligence"] >= computerCurrentCardStats["intelligence"]:
                print("\nYOU WON!!")
                playerNoOfCards += 1
                computerNoOfCards -= 1
                computerStatList.remove(computerCurrentCardStats)
                playerStatList.append(computerCurrentCardStats)
                winner = "player"
            elif playerCurrentCardStats['intelligence'] < computerCurrentCardStats['intelligence']:
                print("\nYOU LOST!!")
                playerNoOfCards -= 1
                computerNoOfCards += 1
                computerStatList.append(playerCurrentCardStats)
                playerStatList.remove(playerCurrentCardStats)
                winner = "computer"
        elif category == 3:
            if playerCurrentCardStats["friendliness"] >= computerCurrentCardStats["friendliness"]:
                print("\nYOU WON!!")
                playerNoOfCards += 1
                computerNoOfCards -= 1
                computerStatList.remove(computerCurrentCardStats)
                playerStatList.append(computerCurrentCardStats)
                winner = "player"
            elif playerCurrentCardStats['friendliness'] < computerCurrentCardStats['friendliness']:
                print("\nYOU LOST!!")
                playerNoOfCards -= 1
                computerNoOfCards += 1
                computerStatList.append(playerCurrentCardStats)
                playerStatList.remove(playerCurrentCardStats)
                winner = "computer"
        elif category == 4:
            if playerCurrentCardStats["drool"] <= computerCurrentCardStats["drool"]:
                print("\nYOU WON!!")
                playerNoOfCards += 1
                computerNoOfCards -= 1
                computerStatList.remove(computerCurrentCardStats)
                playerStatList.append(computerCurrentCardStats)
                winner = "player"
            elif playerCurrentCardStats['drool'] > computerCurrentCardStats['drool']:
                print("\nYOU LOST!!")
                playerNoOfCards -= 1
                computerNoOfCards += 1
                computerStatList.append(playerCurrentCardStats)
                playerStatList.remove(playerCurrentCardStats)
                winner = "computer"
        if playerNoOfCards == 0 or computerNoOfCards == 0: loopCtrl = 3


start = menu()

if start:
    nOC, pNOC, pSL, cNOC, cSL = setup()
    gameplay(nOC, pNOC, pSL, cNOC, cSL)


# BIG EOF COMMENT!!!
"""
I need to add error handling to all inputs, and I need to make what the player sees more succinct, as well as tidying up
my code to make it more readable, and to trim anything that isn't actually needed

I then need to add comments to any line that's function isn't obvious
"""