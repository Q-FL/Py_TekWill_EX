import csv
def fishInfo():
	fishlis = []
	with open('zoo_data.csv') as zooData:
		reader = csv.reader(zooData)
		for r in reader:
			if r[0] == 'fishes':
				fishlis.append(r)
	return fishlis