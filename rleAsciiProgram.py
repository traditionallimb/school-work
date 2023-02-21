def menu():
	loopCtrl = 1
	print("========== RLE <-> ASCII==========")
	print("\t1. Enter RLE\n\t2. Display ASCII Art\n\t3. Convert to ASCII art\n\t4. Convert to RLE\n\t5. Quit")
	while loopCtrl == 1:
		loopCtrl = 2
		userOpt = input("Enter a number > ")
		try:
			int(userOpt)
		except:
			print("That isn't a number, please try again.")
			loopCtrl = 1
		try:
			userOpt in range(1, 5)
		except:
			print("That number is not an actual option, please try again.")
			loopCtrl = 1



menu()
