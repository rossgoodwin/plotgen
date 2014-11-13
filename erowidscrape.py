import requests
from bs4 import BeautifulSoup

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

# scrape URLs...
for url in erowidURLsBy1000[indx]:
	# split at =
	urlSplit = url.split('=')
	# last part is urlID
	urlID = urlSplit[-1]

	# try, except anything...
	try:
		# get url and extract text...
		r = requests.get(url+"&format=latex")
		doc = r.text

		# print confirmation message
		print "RETRIEVING:\t"+urlID

		# write to file...
		ffff = open('erowid_experience/'+str(indx)+'/'+urlID+'.txt', 'w')
		ffff.write(doc.encode('utf8'))
		ffff.close()
	except:
		pass