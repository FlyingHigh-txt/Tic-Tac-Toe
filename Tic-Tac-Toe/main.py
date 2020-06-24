import random

row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
#Functions
def Move(move):
	move = str(move)
	if "1" in move or "2" in move or "3" in move:
		return 1
	elif "4" in move or "5" in move or "6" in move:
		return 2
	elif "7" in move or "8" in move or "9" in move:
		return 3
	else:
		return 4

#------------------

def checkMove(move, row1, row2, row3):
	if Move(move) == 1:
		move = int(move)
		if row1[move-1] == "X" or row1[move-1] == "O":
			return 1
	if Move(move) == 2:
		move = int(move)
		if row2[move-4] == "X" or row2[move-4] == "O":
			return 1
	if Move(move) == 3:
		move = int(move)
		if row3[move-7] == "X" or row3[move-7] == "O":
			return 1

#---------------------

def checkWin(row1, row2, row3):
	if (row1[0] == "X") and (row1[1] == "X") and (row1[2] == "X"):
		return 1
	if (row2[0] == "X") and (row2[1] == "X") and (row2[2] == "X"):
		return 1
	if (row3[0] == "X") and (row3[1] == "X") and (row3[2] == "X"):
		return 1
	if (row1[0] == "X") and (row2[0] == "X") and (row3[0] == "X"):
		return 1
	if (row1[1] == "X") and (row2[1] == "X") and (row3[1] == "X"):
		return 1
	if (row1[2] == "X") and (row1[2] == "X") and (row1[2] == "X"):
		return 1
	if (row1[0] == "X") and (row2[1] == "X") and (row3[2] == "X"):
		return 1
	if (row1[2] == "X") and (row2[1] == "X") and (row3[0] == "X"):
		return 1
	if (row1[0] == "O") and (row1[1] == "O") and (row1[2] == "O"):
		return 2
	if (row2[0] == "O") and (row2[1] == "O") and (row2[2] == "O"):
		return 2
	if (row3[0] == "O") and (row3[1] == "O") and (row3[2] == "O"):
		return 2
	if (row1[0] == "O") and (row2[0] == "O") and (row3[0] == "O"):
		return 2
	if (row1[1] == "O") and (row2[1] == "O") and (row3[1] == "O"):
		return 2
	if (row1[2] == "O") and (row1[2] == "O") and (row1[2] == "O"):
		return 2
	if (row1[0] == "O") and (row2[1] == "O") and (row3[2] == "O"):
		return 2
	if (row1[2] == "O") and (row2[1] == "O") and (row3[0] == "O"):
		return 2
	


#Game Board Print
for i in row1:
	print(i, end=" ")
print()
for i in row2:
	print(i, end=" ")
print()
for i in row3:
	print(i, end=" ")
print()

game = True
turns = 9
while game == True:
	mode  = input("Would you like to play the computer, 'c', or another player, '2'? ").lower()
	if mode == "2":	
		while turns > 0:
			#Player One
			firstPlayer = True
			while firstPlayer == True:
				p1 = input("Player one, where would you like to move? ")
				p1 = int(p1)
				if checkMove(p1, row1, row2, row3) == 1:
					print("That spot already has already been played on.")
					continue
				fp = Move(p1)
				if fp == 1:
					row1[p1-1] = "X"
				elif fp == 2:
					row2[p1-4] = "X"
				elif fp == 3:
					row3[p1-7] = "X"
				else:
					print("You must enter a number on the board")
					continue
				firstPlayer = False


				turns -= 1

				#Game Board Print
				for i in row1:
					print(i, end=" ")
				print()
				for i in row2:
					print(i, end=" ")
				print()
				for i in row3:
					print(i, end=" ")
				print()

			Win = checkWin(row1, row2, row3)
			if Win == 1:
				print("Player One has Won!")
				break

			if turns == 0:
				break

			#Player 2
			secondPlayer = True
			while secondPlayer == True:	
				p2 = input("Player two, where would you like to move? ")
				p2 = int(p2)
				if checkMove(p2, row1, row2, row3) == 1:
					print("That spot already has already been played on.")
					continue
				sp = Move(p2)
				if sp == 1:
					row1[p2-1] = "O"
				elif sp == 2:
					row2[p2-4] = "O"
				elif sp == 3:
					row3[p2-7] = "O"
				else:
					print("You must enter a number on the board")
					continue


				turns -= 1

				#Game Board Print
				for i in row1:
					print(i, end=" ")
				print()
				for i in row2:
					print(i, end=" ")
				print()
				for i in row3:
					print(i, end=" ")
				print()
				secondPlayer = False

			Win = checkWin(row1, row2, row3)
			if Win == 2:
				print("Player Two has Won!")
				break

	elif mode == "c":
		who = input("Would you like to go, 'i', or computer, 'c'? ").lower()
		if who == 'i':
			while turns > 0:
				#Player One
				firstPlayer = True
				while firstPlayer == True:
					p1 = input("Where would you like to move? ")
					p1 = int(p1)
					if checkMove(p1, row1, row2, row3) == 1:
						print("That spot already has already been played on.")
						continue
					fp = Move(p1)
					if fp == 1:
						row1[p1-1] = "X"
					elif fp == 2:
						row2[p1-4] = "X"
					elif fp == 3:
						row3[p1-7] = "X"
					else:
						print("You must enter a number on the board")
						continue
					
					turns -= 1

					firstPlayer = False


				Win = checkWin(row1, row2, row3)
				if Win == 1:
					print("You Won!")
					break

				if turns == 0:
					break
				#Computer
				Computer = True
				while Computer == True:	
					cmove = random.randint(1,9)
					if checkMove(cmove, row1, row2, row3) == 1:
						continue
					sp = Move(cmove)
					if sp == 1:
						row1[cmove-1] = "O"
					elif sp == 2:
						row2[cmove-4] = "O"
					elif sp == 3:
						row3[cmove-7] = "O"


					turns -= 1

					#Game Board Print
					for i in row1:
						print(i, end=" ")
					print()
					for i in row2:
						print(i, end=" ")
					print()
					for i in row3:
						print(i, end=" ")
					print()
					Computer = False

				Win = checkWin(row1, row2, row3)
				if Win == 1:
					print("You lost :(")
					break
		elif who == 'c':
			#Computer
			Computer = True
			while Computer == True:	
				cmove = random.randint(1,9)
				if checkMove(cmove, row1, row2, row3) == 1:
					continue
				sp = Move(cmove)
				if sp == 1:
					row1[cmove-1] = "X"
				elif sp == 2:
					row2[cmove-4] = "X"
				elif sp == 3:
					row3[cmove-7] = "X"
				turns -= 1
				#Game Board Print
				for i in row1:
					print(i, end=" ")
				print()
				for i in row2:
					print(i, end=" ")
				print()
				for i in row3:
					print(i, end=" ")
				print()
				Computer = False
			Win = checkWin(row1, row2, row3)
			if Win == 2:
				print("You lost :(")
				break
			#Player One
			firstPlayer = True
			while firstPlayer == True:
				p1 = input("Where would you like to move? ")
				p1 = int(p1)
				if checkMove(p1, row1, row2, row3) == 1:
					print("That spot already has already been played on.")
					continue
				fp = Move(p1)
				if fp == 1:
					row1[p1-1] = "X"
				elif fp == 2:
					row2[p1-4] = "X"
				elif fp == 3:
					row3[p1-7] = "X"
				else:
					print("You must enter a number on the board")
					continue
				firstPlayer = False
				turns -= 1

			Win = checkWin(row1, row2, row3)
			if Win == 2:
				print("You Won!")
				break
			if turns == 0:
				break
	game = False