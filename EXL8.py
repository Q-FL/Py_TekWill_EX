import os

#EX1: Calculate sum of size all .py files in your working directory. Convert in in MegaBytes.
def ex1():
	files = os.scandir('.')
	lis = []
	lis2 = []
	for i in files:
		a = i.name
		if a[-3:] == '.py':
			lis.append(a)
			y = i.stat()
			lis2.append(y.st_size)

	print(f'There are: {len(lis)} .py files',
		f'\nSum size in MegaBytes: {str(sum(lis2)/1000000)}')

#EX2: Find name of last modified file in your current working directory.
def ex2():
	lis = []
	for i in os.scandir('.'):
		i = i.stat()
		lis.append(i.st_mtime)
		lis.sort()
	for n in os.scandir('.'):
		ns = n.stat()
		if ns.st_mtime == lis[-1]:
			print(f'Last modified file: {n.name} {lis[-1]}')

#EX3: Find name of last accessed filed your current working directory.
def ex3():
	lis = []
	for i in os.scandir('.'):
		i = i.stat()
		lis.append(i.st_atime)
		lis.sort()
	for n in os.scandir('.'):
		ns = n.stat()
		if ns.st_atime == lis[-1]:
			print(f'Last accessed file: {n.name} {lis[-1]}')

#EX4: Create my_data_folder
def ex4():
	def datacolector():
		while True:
			name = input('Name: ')
			if name.isalpha():
				age = input('Age: ')
				if age.isdigit():
					occupation = input('Occupation: ')
					return {'name':name, 'age':age, 'occupation':occupation}
					break
				else:
					print('ERROR - Incorect Age Format')
			else:
				print('ERROR - Incorect Name Format !')

	data = datacolector()
	name = data['name']
	age = data['age']
	occupation = data['occupation']

	os.mkdir('my_data_folder')
	os.chdir('my_data_folder')

	write = open('client_data.txt', 'w')
	write.writelines([f'Name: {name}',
		f'\nAge: {age}',
		f'\nOccupation: {occupation}'])

	print('Data folder created and updated successefuly !')

while True:
	exercitiul = input('Alegeti exercitiul 1-4: ')
	if exercitiul == '1':
		print('\nTask - Calculate sum size of all .py files in your working directory. Convert in MegaBytes.')
		ex1()
		print('')
	if exercitiul == '2':
		print('\nTask - Find name of last modified file in your current working directory.')
		ex2()
		print('')
	if exercitiul == '3':
		print('\nTask - Find name of last accessed filed your current working directory.')
		ex3()
		print('')
	if exercitiul == '4':
		print('\nTask - Create my_data_folder with user input data.')
		ex4()
		print('')
	if exercitiul == 'exit':
		break
	print('Pentru a iesi, tapati "exit"')