print('#~~~~~~~~~~~~~~~# Exercitii lectia 6 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#','\n','\n',
	'           Selectati exercitul de la 1-8','\n',
	'\n EX1:  Sarcina - Scrieti o functie care sa gaseasca maximum 3 numere.',
	'\n EX2:  Sarcina - Scrieti o functie care sa calculeze produsul elementelor unei liste.',
	'\n EX3:  Sarcina - Scrieti o functie care sa calculeze numarul de litere majuscule si ',
	'\n                 minuscule dintr-un text.',
	'\n EX4:  Sarcina - Scrieti o functie care sa intoarca elementele distincte dintr-o lista.',
	'\n EX5:  Sarcina - Scrieti o functie care calculeaza daca un numar este prim.',
	'\n EX6:  Sarcina - Scrieti o functie care afiseaza o secventa de numere Fibonacci.',
	'\n EX7:  Sarcina - Scrieti o functie care valideaza o adresa de email.',
	'\n EX8:  Sarcina - Scrieti o functie care in caz de exceptie afiseaza un mesaj de',
	'\n                 erroare si cheama functia de convertire din nou.')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')


#EX1: Scrieti o functie care sa gaseasca maximum 3 numere
def ex1():
	while True:
		def nr(nr1,nr2,nr3):
			lista = [nr1,nr2,nr3]
			print(f'Ati indicat {len(lista)} numere, bravo !')

		i = input('Scrieti maximum 3 numere: ')
		if i.find(',') > 0:
			i = i.split(',')
			if len(i) == 3:
				if i[0].isdigit() and i[1].isdigit() and i[2].isdigit():
					a,b,c = i[0],i[1],i[2]
					nr(a,b,c)
					break
				else:
					print('ERROR - Ati adaugat caractere in plus, indicati doar 3 numere intregi !')
			else:
				print('ERROR - Indicati 3 numere intregi !')
		else:
			print('ERROR - Indicati 3 numere intregi prin virgula !')


#EX2: Scrieti o functie care sa calculeze produsul elementelor unei liste.
def ex2():
	while True:
		def produsul(*x):
			suma = 1
			for i in x:
				try:
					suma = suma * float(i)
				except ValueError:
					pass
			print(f'Rezultat: {round(suma)}')

		lista = input('Introduceti un sir de numere (nr,nr,nr): ')
		if lista.find(',') > 0:
			lista = lista.split(',')
			produsul(*(lista))
			break
		else:
			print('ERROR - Lista trebuie sa contina minim 2 numere (nr,nr,nr) !')


#EX3: Scrieti o functie care sa calculeze numarul de litere majuscule si minuscule dintr-un text
def ex3():
	x = input('Introduceti un text: ')
	lisA = []
	lisa = []
	for i in x:
		if i.isupper():
			lisA.append(i)
		if i.islower():
			lisa.append(i)
	print(f'Litere majuscule: {len(lisA)} Litere minuscule: {len(lisa)}')


#EX4: Scrieti o functie care sa intoarca elementele distincte dintr-o lista. Ex: ([1,2,3,3,3,3,4,5] - > [1, 2, 3, 4, 5])
def ex4():
	def e_distinct(x):
		d = set(x)
		print(f'Lista elementelor distincte: {list(d)}')
	lista = [1,1,2,3,3,3,4,5,5,5,5,5]
	print(f'Lista elementelor: {lista}')
	e_distinct(lista)


#EX5: Scrieti o functie care calculeaza daca un numar este prim.
def ex5():
	while True:
		nru = int(input('Introduceti nr: '))
		lis = []
		for i in range(2,nru):
			if nru % i == 0:
				lis.append(i)
				break
		if lis != []:
			print('Numarul nu este prim !',
				f'\nPrimul numar la care se v-a imparte {nru} este: {lis}',
				'\nMai incearca !')
		else:
			print(f'Numarul: {nru} este prim !!!')
			break


#EX6 Scrieti o functie care afiseaza o secventa de numere Fibonacci 
def ex6():
	while True:
		n = input('Indicati cite numere din secventa Fibonacci doriti: ')
		if n.isdigit():
			n = int(n)
			if n>0:
				if n == 1:
					print('Secventa Fibonacci:',[0])
					break
				elif n == 2:
					print('Secventa Fibonacci:',[0,1])
					break
				else:
					f1,f2 = 0,1
					lis = []
					for i in range(n-2):
						calc = f1 + f2
						f1 = f2
						f2 = calc
						lis.append(calc)
					lis.insert(0,1)
					lis.insert(0,0)
					print('Secventa Fibonacci:',lis)
					break
			else:
				print('ERROR - Numarul trebuie sa fie pozitiv !')
		else:
			print('ERROR - Indicati un numar intreg pozitiv !')


#EX7:Scrieti o functie care valideaza o adresa de email
def ex7():
	import re
	while True:
		email = input('Introduceti adresa de email: ')
		if (re.search(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email)):
			print(f'Adresa de Email {email} este valida !')
			break
		else:
			print('ERROR - Adresa de Email nu-i valid, mai incearca !')


#EX8: Scrieti o functie care primeste la input un text cu cifre si il converteste
#     in numar, in caz de exceptie (este introdus o litera), afisati un
#     mesaj de erroare si chemati functia de convertire din nou.
def ex8():
	while True:
		text =  input('Introduceti numar integer: ')
		try:
			text = int(text)
			print(f'Numarul {text} este integer !')
			break
		except ValueError:
			print('ERROR - Au fost introduse simboluri interzise, mai incearca !')

# Interface:

while True:
	exercitiul = input('Alegeti exercitiul 1-8: ')
	if exercitiul == '1':
		print('')
		print('EX1: Scrieti o functie care sa gaseasca maximum a 3 numere')
		ex1()
		print('')
	if exercitiul == '2':
		print('')
		print('EX2: Scrieti o functie care sa calculeze produsul elementelor unei liste.')
		ex2()
		print('')
	if exercitiul == '3':
		print('')
		print('EX3: Scrieti o functie care sa calculeze numarul de litere majuscule si minuscule dintr-un text.')
		ex3()
		print('')
	if exercitiul == '4':
		print('')
		print('EX4: Scrieti o functie care sa intoarca elementele distincte dintr-o lista.')
		ex4()
		print('')
	if exercitiul == '5':
		print('')
		print('EX5: Scrieti o functie care calculeaza daca un numar este prim.')
		ex5()
		print('')
	if exercitiul == '6':
		print('')
		print('EX6: Scrieti o functie care afiseaza o secventa de numere Fibonacci.')
		ex6()
		print('')
	if exercitiul == '7':
		print('')
		print('EX7: Scrieti o functie care valideaza o adresa de email.')
		ex7()
		print('')
	if exercitiul == '8':
		print('')
		print('EX8: Scrieti o functie care in caz de exceptie afiseaza un mesaj de erroare si cheama functia de convertire din nou.')
		ex8()
		print('')
	if exercitiul == 'exit':
		break

	print('Pentru a iesi, tapati "exit"')