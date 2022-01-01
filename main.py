import random
import os
clearConsole = lambda: print('\n'* 150)


br = "\n"

global guess
def letterGuess():
	global guess
	count = 0
	print("Word: "+br)
	for i in lettersCorrect:
		print(i , end = '')
	print(br)
	if(len(lettersGuessed)> 0):
		print("Letters Guessed: "+br)
	for i in lettersGuessed:
		count += 1
		if(count == 1):
			print("[",end = '')
		print(i , end = '')
		if(count == len(lettersGuessed)):
			print("]", end = '')
	while(1):
		print(br)
		guess = input(" Enter in a character "+ br)
		if(guess.isalpha() and guess not in lettersGuessed):
			break
		elif(guess in lettersGuessed):
			print(" you have already guessed that letter")
		else:
			continue


print("*****Welcome to Hangman*****")


hangmanText = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ["snake","tiger","lion","seel","zebra","monkey","birds","wolf"]

dictionary = {
  0: words[0],
	1: words[1],
	2: words[2],
	3: words[3],
	4: words[4],
	5: words[5],
	6: words[6],
	7: words[7],

}

lettersGuessed = []
lettersCorrect = []
numberIncorrect = 0
randomNumber = random.randint(0, len(words)-1)
word = dictionary[randomNumber]
for i in range(len(word)):
	lettersCorrect.append("_")
wordLength = len(word)
solidWord = word

while('_' in lettersCorrect):
	letterGuess()
	guess = guess[0].lower()
	if(numberIncorrect == len(hangmanText)-1):
		break
	if(guess in solidWord):
		spot = 0
		for i in solidWord:
			if(guess == i):
				lettersCorrect[spot]=i
			spot +=1 
		if(guess in word):	
			word = word.replace(guess,"")
			lettersGuessed.append(guess)
			clearConsole()
			print(" CORRECT " + br)
			print(hangmanText[numberIncorrect])
	else:
		lettersGuessed.append(guess)
		numberIncorrect += 1
		clearConsole()
		print(" INCORRECT " + br)
		print(hangmanText[numberIncorrect])


if(numberIncorrect == len(hangmanText)-1):
	clearConsole()
	print(hangmanText[numberIncorrect])
	print(br+ " The word was "+ solidWord)

	print(" LUSER ")
else:
	clearConsole()
	print(" WINNER ")
	print(br+ " The word was "+ solidWord)
