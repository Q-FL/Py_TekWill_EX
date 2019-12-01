# Creates a file with some data:
with open('EXL9_Data-Sample.txt','w') as wr:
	for v in range(10):
		wr.write(f'\nNumber: {v}')
	wr.close()

# Write a program that will count number of lines in a file:
with open('EXL9_Data-Sample.txt','r') as rl:
	print('Number of lines:',len(rl.readlines()))
	rl.close()

# Write a program that will count frequency of a word in a file (word will be "Number"):
repeat = []
with open('EXL9_Data-Sample.txt','r') as rt:
	for lines in rt.readlines():
		if lines.find('Number') != -1:
			repeat.append(1)
	rt.close()
print('Number of "Number" words:',len(repeat))

# Write a program that will append new content to the end of a file. (Content will be word "Nova1")
with open('EXL9_Data-Sample.txt','a+') as ap:
	ap.write('\nNova1')
	ap.seek(0)
	print('Added "Nova1":',ap.read())

# Write a program that will remove newline character from a file.
with open('EXL9_Data-Sample.txt','r') as rplc:
	dats = rplc.read()
	with open('EXL9_Data-Sample.txt','w') as wrn:
		wrn.write(dats.replace('\n',''))

# Prints the finished data format in file.
with open('EXL9_Data-Sample.txt','r') as rd:
	print(rd.read())