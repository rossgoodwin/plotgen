import csv
import random

def makenamelists():
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
	return [firstnames_m, firstnames_f, surnames]

name_lists = makenamelists()

fnames_m = ['\"'+name+'\"' for name in name_lists[0]]
fnames_f = ['\"'+name+'\"' for name in name_lists[1]]
lnames = ['\"'+name+'\"' for name in name_lists[2]]

opener0 = "mFirstNames = ["
opener1 = "fFirstNames = ["
opener2 = "surnames = ["
closer = "]"


f_fn_m = open('firstnames_m.txt', 'w')
f_fn_m.write(opener0+','.join(fnames_m)+closer)

f_fn_f = open('firstnames_f.txt', 'w')
f_fn_f.write(opener1+','.join(fnames_f)+closer)

f_ln = open('surnames.txt', 'w')
f_ln.write(opener2+','.join(lnames)+closer)
