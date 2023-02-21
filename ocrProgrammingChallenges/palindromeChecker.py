userInput = str(input("Enter a word to check if it a palindrome: > "))
reversedWordString = userInput[::-1]
if reversedWordString in userInput: print(f"'{userInput}' is a palindrome!")
elif reversedWordString not in userInput: print(f"'{userInput}' is not a palindrome! '{userInput}' backwards is {reversedWordString}.")