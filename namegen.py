import csv
import random

surnames = []
with open('surnames/app_c.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		surnames.append(row[0].capitalize())

firstnames_m = []
firstnames_f = []
for year in range(1880, 2014):
	ff = open('names/yob'+str(year)+'.txt', 'r')
	for line in ff:
		line_list = line.split(",")
		name = line_list[0]
		if line_list[1] == 'M':
			firstnames_m.append(name.capitalize())
		elif line_list[1] == 'F':
			firstnames_f.append(name.capitalize())

for _ in range(50):
	print random.choice(firstnames_f) + " " + random.choice(surnames)
		