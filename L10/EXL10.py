#EX1: Calculate when python course ends. Start date (28.10.2019) + 15 weeks + 8 days of vacation.
from datetime import date, timedelta

finish_date = date(2019,10,28) + timedelta(weeks=15,days=10)
print('End date of Py-Course: ',finish_date,'\n')

#EX2: Write a program which randomly picks an integer from 1 to 100. Your program
# should prompt the user for guesses – if the user guesses incorrectly, it should
# print whether the guess is too high or too low. If the user guesses correctly,
# the program should print how many guesses the user took to guess the right
# answer. You can assume that the user will enter valid input.

import random

def guessTheNumber():
	rand_nr = random.randint(1,100)
	print(rand_nr)
	count_tryes = 1
	while True:
		user_guess = input('Guess the number: ')
		if user_guess.isdigit():
			if int(user_guess) == rand_nr:
				print(f'YAY ! Tryes: {count_tryes}')
				break
			if int(user_guess) < rand_nr:
				print('Nope... its higher !')
				count_tryes += 1
			if int(user_guess) > rand_nr:
				print('Nope... its lower !')
				count_tryes += 1
		else:
			print('ERROR - Input natural number')
guessTheNumber()

#EX3: Download content of 999.md site, calculate how many urls are present on it.


import requests as rqs
url = 'https://999.md/ro/'
url_data = rqs.get(url).text
https_count = url_data.count('https')
print(f'\nFound: {https_count} "https" in {url}')