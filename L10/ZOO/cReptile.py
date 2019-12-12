import csv
def reptileInfo():
	reptilelis = []
	with open('zoo_data.csv') as zooData:
		reader = csv.reader(zooData)
		for r in reader:
			if r[0] == 'reptiles':
				reptilelis.append(r)
	return reptilelis