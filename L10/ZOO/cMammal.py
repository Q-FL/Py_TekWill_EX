import csv
def mammalInfo():
	mammallis = []
	with open('zoo_data.csv') as zooData:
		reader = csv.reader(zooData)
		for r in reader:
			if r[0] == 'mammals':
				mammallis.append(r)
	return mammallis