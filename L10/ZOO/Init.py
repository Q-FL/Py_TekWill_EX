import ZOO,cBirds,cFish,cReptile,cMammal

def birdsLife():
	birds_lis = cBirds.birdsInfo()
	for r in birds_lis:
		print(ZOO.zoO(r[0],r[1],r[2]))
		print(ZOO.zoO.getAgeInfo(r[1],r[2]))
def fishLife():
	fish_lis = cFish.fishInfo()
	for r in fish_lis:
		print(ZOO.zoO(r[0],r[1],r[2]))
		print(ZOO.zoO.getAgeInfo(r[1],r[2]))
def reptileLife():
	reptile_lis = cReptile.reptileInfo()
	for r in reptile_lis:
		print(ZOO.zoO(r[0],r[1],r[2]))
		print(ZOO.zoO.getAgeInfo(r[1],r[2]))
def mammalLife():
	mammal_lis = cMammal.mammalInfo()
	for r in mammal_lis:
		print(ZOO.zoO(r[0],r[1],r[2]))
		print(ZOO.zoO.getAgeInfo(r[1],r[2]))

while True:
	user_input = input('Chose one class of animals (1-4): ')
	if user_input == '1':
		print('')
		print('Class: Birds')
		birdsLife()
		print('')
	if user_input == '2':
		print('')
		print('Class: Fish')
		fishLife()
		print('')
	if user_input == '3':
		print('')
		print('Class: Reptile')
		reptileLife()
		print('')
	if user_input == '4':
		print('')
		print('Class: Mammal')
		mammalLife()
		print('')
	if user_input == 'exit':
		break
	print('Pentru a iesi, tapati "exit"')