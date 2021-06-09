from random import randint
from time import sleep as sp
from os import system as sy

def clearScreen():
	sy('clear') or None

def userInput(message: int) -> int:
	return int(input(f'{message} '))

def generatorNum():
	generator = randint(1, 100)
	return generator
	
def game(number, attempts):
	while True:
		try:
			guess = userInput('\nkick a number between 1 and 100.\nAnswer:')
			if guess > 100 or guess < 1:
				sp(1)
				print('\njust a number between 1 and 100. Try again!')
			elif guess > number:
				sp(1)
				print(f'\nthe number I thought is less than {guess}. Try again!')
				attempts += 1
				sp(1)
			elif guess < number:
				sp(1)
				print(f'\nthe number I thought is greater than {guess}. Try again!')
				attempts += 1
				sp(1)
			elif guess == number:
				sp(1)
				print(f'\nCONGRATULATIONS, you got it right with {attempts} attempts!')
				sp(1)
				option = input('Do you want to play again? [y/n]: ')
				if option.lower() == 'y' or option.lower() == 'yes':
					sp(1)
					print('Restarting the game...')
					sp(1)
					number = generatorNum()
					attempts = 0
					clearScreen()
					continue
				elif option.lower() == 'n' or 'no':
					sp(1)
					print('Ok, thanks for playing')
					break
		except ValueError:
			print('[i] The value entered must be an integer!')

def main():
	input('[i] press ENTER to start...')
	number = generatorNum()
	print(number)
	attempts = 0
	game(number, attempts)
	
if __name__ == '__main__':
	main()