from sys import argv
import csv
import random
import requests
from bs4 import BeautifulSoup

# script, _url = argv


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


def scrape(url):
	r = requests.get(url)
	doc = r.text
	soup = BeautifulSoup(doc)
	wikitext = soup.find(id="wikitext")
	approvedTags = ["em", "strong", "a", "ul", "ol", "li"]
	scraped = []
	for c in wikitext.children:
		try:
			tagClass = c['class']
		except TypeError:
			tagClass = False
		except KeyError:
			tagClass = False
		except AttributeError:
			tagClass = False

		try:
			childTag = c.name
		except TypeError:
			childTag = False
		except KeyError:
			childTag = False
		except AttributeError:
			childTag = False

		if childTag and childTag not in approvedTags:
			pass
		elif childTag and childTag in approvedTags:
			if tagClass:
				if tagClass[0] == "twikilink":
					scraped.append(c.string.lower())
				elif tagClass[0] == "urllink":
					scraped.append(c.contents[0])
			elif childTag == "ul" or childTag == "ol":
				for d in c.children:
					scraped.append(d.contents[0])
			else:
				scraped.append(c.string)

		else:
			scraped.append(c)

	bad_values = ['\n', None]
	scraped = [s for s in scraped if not s in bad_values]

	article = "".join(scraped)
	article = article.split('\n')
	article = '\n\n'.join(article)

	return article


def geturllist(url):
	r = requests.get(url)
	doc = r.text
	soup = BeautifulSoup(doc)
	wikitext = soup.find(id="wikitext")
	lis = wikitext.find_all('li')

	# dat shit clean...
	links = [l.find_all('a')[0] for l in lis]
	hrefs = [l.get('href') for l in links]
	# ...awww yeah

	return hrefs

# print geturllist("http://tvtropes.org/pmwiki/pmwiki.php/Main/Heroes")

def makefiles(urls):
	filenames = []
	for kind, _url in urls.iteritems():
		char_urls = geturllist(_url)

		# print char_urls

		for u in char_urls:
			name = u.split('/')[-1]
			#article = scrape(u)
			filenames.append("tropes_character/"+kind+"/"+name+".txt")
			#ffff = open("tropes_character/"+kind+"/"+name+".txt", "w")
			#ffff.write(article.encode('utf8'))
			#ffff.close()
	print filenames

urls_dict = {}

# urls_dict['villains'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/Villains"
# urls_dict['heroes'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/Heroes"
# urls_dict['general'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/Characters"

#urls_dict['perverts'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/TropesAboutPerverts"
urls_dict['plotrelated'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/CharacterizationTropes"
#urls_dict['pure'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/PurityPersonified"
urls_dict['other'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/OthernessTropes"
urls_dict['alone'] = "http://tvtropes.org/pmwiki/pmwiki.php/Main/SolitaryTropes"


makefiles(urls_dict)





