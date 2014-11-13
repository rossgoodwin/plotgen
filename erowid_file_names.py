# import erowidURLs var
from erowid_experience import *

# partition list
erowidURLsBy1000 = []

# current folder
indx = 18

# split erowidURLs into 19 pieces...
for i in range(18):
	erowidURLsBy1000.append(erowidURLs[i*1000:(i+1)*1000])
erowidURLsBy1000.append(erowidURLs[18000:])

erowidPaths = []

for i in range(len(erowidURLsBy1000)):
	if i < 10:
		folder = '0' + str(i)
	else:
		folder = str(i)

	for j in range(len(erowidURLsBy1000[i])):
		url = erowidURLsBy1000[i][j]
		urlSplit = url.split('=')
		urlID = urlSplit[-1]
		erowidPaths.append('erowid_experience/'+folder+'/'+urlID+'.txt')

print erowidPaths