print('#~~~~~~~~~~~~~~~# Exercitii lectia 4 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#','\n','\n',
	'           Selectati exercitul de la 1-10','\n','\n',
	'EX1:  Sarcina - Suma numerelor pare mai mici decit 100','\n',
	'EX2:  Sarcina - Conversiunea gradelor','\n',
	'EX3:  Sarcina - Cuvint palindrom','\n',
	'EX4:  Sarcina - Scrieti un program care sa afiseze toti divizorii unui numar intreg','\n',
	'EX5:  Sarcina - Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest la 5 si 7.','\n',
	'EX6:  Sarcina - Program care sa primeasca la input un numar intreg si sa creeze un dictionar care contine','\n',
	'                numere mai mici sau egale decit N si N**2.','\n',
	'EX7:  Sarcina - Scrieti un program care sa calculeze numarul de litere si cifre dintr-un text.','\n',
	'EX8:  Sarcina - Scrieti un program care verifica daca o parola introdusa de utilizator este securizata.','\n',
	'EX9:  Sarcina - Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o propozitie.','\n',
	'EX10: Sarcina - Scrieti un program care sa elimine cuvinte duplicate dintr-o propozitie.')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')

#EX2: Suma numerelor pare mai mici decit 100
def exec1():
	while True:
		nr = input('Scrieti primul numar intreg par < 100: ')
		nr2 = input('Scrieti al doilea numar intreg par < 100: ')
		if str.isdigit(nr) and str.isdigit(nr2):
			nr = float(nr)
			nr2 = float(nr2)

			if nr <= 100 and nr2 <= 100:
				if nr % 2 == 0 and nr2 % 2 == 0:
					calc = round(nr + nr2)
					print(f'Suma: {calc}')
					print('')
					break

		print('ERROR: Numarul trebuie sa fie intreg par < 100, mai incearca !')

#EX3: Conversiunea gradelor
def exec2():
	while True:
		grade = input('Grade: ')

		if grade.isdigit():
			grade = float(grade)
			tip_grade = input('Alegeti tipul de grade "c"/"f": ')

			if tip_grade == 'c' or tip_grade == 'C':
				calc_c = round((1.8 * grade) + 32, 3)
				print(f'{grade} Celsius va fi: {calc_c} Fahrenheit')
				print('')
				break
			if tip_grade == 'f' or tip_grade == 'F':
				calc_f = round(((grade - 32) * 5) / 9, 3)
				print(f'{grade} Fahrenheit va fi: {calc_f} Celsius')
				print('')
				break

			print('ERROR: Indicati tipul de grade "c"/"f" !')
		else:
			print('ERROR: Indicati gradele in numar intreg !')

#EX4: Cuvint palindrom
def exec3():
	while True:
		cuvint = input('Scrieti un cuvint: ')
		if cuvint == cuvint[::-1]:
			print(f'Cuvintul "{cuvint}" este palindrom !')
			print('')
			break
		print(f'Cuvintul "{cuvint}" nu este palindrom, mai incearca !')

#EX4: Scrieti un program care sa afiseze toti divizorii unui numar intreg.
def exec4():
	while True:
		nr = input('Scriet un numar intreg: ')
		if nr.isdigit():
			lists = []
			for i in range(1,int(nr)+1):
				if int(nr) % i == 0:
					lists.append(i)
			print('Divizorii sunt: ',lists)
			break
		else:
			print('ERROR - Formatul este gresit, mai incearca !')

#EX5: Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest la 5 si 7.
def exec5():
	lista5 = []
	lista7 = []
	for i in range(1000,2300):

		if i % 5 == 0:
			lista5.append(i)

		if i % 7 == 0:
			lista7.append(i)
	calc5 = sum(lista5)
	calc7 = sum(lista7)
	print(f'Suma numerelor ce se impart fara rest la 5: {calc5}')
	print(f'Suma numerelor ce se impart fara rest la 7: {calc7}')
	print('')

#EX6: Program care sa primeasca la input un numar intreg si sa creeze un dictionar care contine numere mai mici sau egale decit N si N**2.
def exec6():
	while True:
		N = input('Indicati un numar intreg: ')
		if str.isdigit(N):
			dic = {}
			for i in range(0,int(N)+1):
				dic[i] = i**2
			print('Numerele mai mici sau egale decit N si N**2 sunt:')
			print(dic)
			break
		else:
			print('ERROR: Indicati Numar Intreg !')

#EX7: Scrieti un program care sa calculeze numarul de litere si cifre dintr-un text.
def exec7():
	text = input('Compune o balada: ')
	cif = []
	lit = []
	for symbols in text:
		if symbols.isdigit():
			cif.append(symbols)
		if symbols.isalpha():
			lit.append(symbols)
	print(f'In text sunt {len(cif)} numere si {len(lit)} litere !')
	print('')

#EX8: Scrieti un program care verifica daca o parola introdusa de utilizator este securizata.
def exec8():
	import re
	while True:
		psw = input('Creati o Parola: ')
		if len(psw) >= 6:
			if(re.search('[a-z]',psw) == None):
				print('ERROR - Parola trebuie sa cotina cel putin o litera din intervalul [a-z] !')
			else:
				if(re.search('[A-Z]',psw)== None):
					print('ERROR - Parola trebuie sa cotina cel putin o litera din intervalul [A-Z] !')
				else:
					if (re.search('[0-9]',psw) == None):
						print('ERROR - Parola trebuie sa cotina cel putin un numar !')
					else:
						if (re.search('[!/#]',psw) == None):
							print('ERROR - Parola trebuie sa contina cel putin unul din caracterele:  !  /  #')
						else:
							if (re.search('[@‘}{ ]',psw) == None):
								print('Parola Acceptata :)')
								print('')
								break
							else:
								print('ERROR - Parola NU trebuie sa contina caracterele:  @  ‘  {  }  " "')
		else:
			print('ERROR - Parola este prea scurta, minim 6 caractere !')

#EX9: Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o propozitie.
def exec9():
	text = 'Când mă gândesc că te gândeşti că mă gândesc la tine gândeşte-te că mă gândesc că te gândeşti la mine.'
	cuvint = 'gândesc'
	print(f'Cuvintul: {cuvint}')
	print(f'Textul: {text}')
	count = []
	for i in text.split():
		if i == cuvint:
			count.append(i)
	print(f'Frecventa cuvintului: {len(count)}')
	print('')

#EX10: Scrieti un program care sa elimine cuvinte duplicate dintr-o propozitie.
def exec10():
	itext = 'Alfabetul limbii române este Alfabetul române totalitatea literelor folosite pentru literelor scrierea Alfabetul limbii române.'
	text = itext.lower()
	propozitie = []
	duplicat = set()
	for cuvint in text.split():
		if cuvint not in duplicat:
			propozitie.append(cuvint)
			duplicat.add(cuvint)

	no_duplicat = ' '.join(propozitie)
	print(f'Textul: {itext}')
	print(f'Textul fara duplicate: {no_duplicat}')
	print('')

# Interface:

while True:
	exercitiul = input('Alegeti exercitiul 1-10: ')
	if exercitiul == '1':
		print('')
		print('EX1: Suma numerelor pare mai mici decit 100.')
		exec1()
	if exercitiul == '2':
		print('')
		print('EX2: Conversiunea gradelor.')
		exec2()
	if exercitiul == '3':
		print('')
		print('EX3: Cuvint palindrom.')
		exec3()
	if exercitiul == '4':
		print('')
		print('EX4: Scrieti un program care sa afiseze toti divizorii unui numar intreg.')
		exec4()
	if exercitiul == '5':
		print('')
		print('EX5: Calculati suma toturor numerelor intre 1000 si 2300 care se impart fara rest la 5 si 7.')
		exec5()
	if exercitiul == '6':
		print('')
		print('EX6: Program care sa primeasca la input un numar intreg si sa creeze un dictionar care contine numere mai mici sau egale decit N si N**2.')
		exec6()
	if exercitiul == '7':
		print('')
		print('EX7: Scrieti un program care sa calculeze numarul de litere si cifre dintr-un text.')
		exec7()
	if exercitiul == '8':
		print('')
		print('EX8: Scrieti un program care verifica daca o parola introdusa de utilizator este securizata.')
		exec8()
	if exercitiul == '9':
		print('')
		print('EX9: Scrieti un program care calculeaza frecventa cu care apare un cuvint intr-o propozitie.')
		exec9()
	if exercitiul == '10':
		print('')
		print('EX10: Scrieti un program care sa elimine cuvinte duplicate dintr-o propozitie.')
		exec10()
	if exercitiul == 'exit':
		break

	print('Pentru a iesi, tapati "exit"')
