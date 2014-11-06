from sys import argv
import requests
from bs4 import BeautifulSoup

script, _url = argv

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

	for i in scraped[:]:
		if i == '\n':
			scraped.remove(i)

	# print scraped

	article = "".join(scraped)
	article = article.split('\n')
	article = '\n\n'.join(article)

	# print article

	return article

print scrape(_url)


