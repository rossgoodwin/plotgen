import requests
import string
from bs4 import BeautifulSoup


def scrape_index(url):
	r = requests.get(url)
	doc = r.text

	urls = []
	splitDoc = doc.split(u'<A HREF=\"subs/exp_')
	for i in range(1,len(splitDoc)):
		x = splitDoc[i]
		indx = string.find(x, '\">')
		urls.append("http://www.erowid.org/experiences/subs/exp_"+x[0:indx])
		print "APPENDING:\t"+x[0:indx]

	return urls


def scrape_subindex():
	urls = scrape_index("http://www.erowid.org/experiences/exp_list.shtml")
	
	expUrls = []

	for url in urls:

		try:
			r = requests.get(url)
			doc = r.text
			splitDoc = doc.split(u'<a href=\"/experiences/exp.php?ID=')

			if len(splitDoc) > 0:
				for i in range(1, len(splitDoc)):
					x = splitDoc[i]
					indx = string.find(x, '\">')
					expUrls.append("http://www.erowid.org/experiences/exp.php?ID="+x[0:indx])
					print "ADDING:\t"+x[0:indx]
		except:
			pass

	return expUrls

for _ in range(50):
	print "\n\n"

print scrape_subindex()

