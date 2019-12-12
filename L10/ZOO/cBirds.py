import csv
def birdsInfo():
	birdslis = []
	with open('zoo_data.csv') as zooData:
		reader = csv.reader(zooData)
		for r in reader:
			if r[0] == 'birds':
				birdslis.append(r)
	return birdslis

		