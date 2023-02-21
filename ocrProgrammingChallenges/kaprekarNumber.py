userInput = int(input("Enter a number to see if it is a Kaprekar Number: >"))
workingNumber = userInput * userInput
workingNumberArray = list(map(int, str(workingNumber)))
workingNumber = 0
for digit in workingNumberArray: workingNumber += digit
if workingNumber == userInput: print(f"{userInput} is a Kaprekar Number!")
elif workingNumber != userInput: print(f"{userInput} is not a Kaprekar Number")
