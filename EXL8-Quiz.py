# Write a program that will generate question for guessing countrie’s capital
# with 4 options of answers.
# 1. Read content of file countries.txt and create a dictionary with country as it’s
# key and capital as value.
# 2. Use random module (import random) in order to get country and it’s capital,
# using same method get another 3 capitals.
# 3. Generate question with 4 options of answer.
# 4. Prompt user for correct answer and display after correct result.
import random
import time
import os

def capital_quiz():
	os.system('clear')

	with open('countries.txt','rb') as file:
		data = (((file.read()).decode('utf-8')).replace('\n',',')).split(',')
		data_dict = {data[i]: data[i + 1] for i in range(0, len(data), 2)}
		file.close()

	total_points = 5
	max_points = 5
	count = 0

	while count < max_points:
		country = random.choices(list(data_dict.keys()),k=4)
		selected_country = country[0]

		print(f'\nQuestion {count+1}: What is the capital of {selected_country} ?')

		random.shuffle(country)

		print(f'1: {data_dict[country[0]]}',
			f'\n2: {data_dict[country[1]]}',
			f'\n3: {data_dict[country[2]]}',
			f'\n4: {data_dict[country[3]]}')

		user_choice = input('\nChose the right answer: ')

		if user_choice.isdigit() and 0 < int(user_choice) < 5:
			user_capital = data_dict[country[int(user_choice)-1]]
			
			if data_dict[selected_country] == user_capital:
				print(f'\nCorrect: {user_capital} is the capital of {selected_country} !')
				count += 1
				time.sleep(2)
				os.system('clear')
			else:
				print(f'\nWrong: Capital of {selected_country} is {data_dict[selected_country]} !')
				count += 1
				total_points -= 1
				time.sleep(2)
				os.system('clear')
		else:
			print('\n! ERROR - Type the number with the right answer 1-4 !')
			time.sleep(2)
			os.system('clear')

	print(f'\nResults: {total_points} out of {max_points}.\n')

os.system('clear')
print('\nWelcome to "Quiz" project.\n\nThere will be 5 questions.\nChose the right answer !')
time.sleep(3)
capital_quiz()