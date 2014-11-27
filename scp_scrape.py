import requests
from bs4 import BeautifulSoup
import json

file_paths = []

def scrape(scp_no):
	url = "http://www.scp-wiki.net/scp-" + str(scp_no)
	r = requests.get(url)
	html_doc = r.text
	soup = BeautifulSoup(html_doc)
	page_content = soup.find(id="page-content")

	article_text = page_content.get_text() # ascii/ignore encode?

	article_list = article_text.split('\n')
	article_list = [p for p in article_list if bool(p) and p[:len("rating:")] != "rating:"]

	if article_list[0] == u"This page doesn't exist yet!" or not bool(article_list):
		pass
	else:
		filePath = 'scp/'+str(scp_no)+'.txt'
		file_paths.append(filePath)
		f = open(filePath, 'w')
		f.write('\n\n'.join(article_list).encode('utf8'))
		f.close()


for i in range(2, 10):
	scrape("00"+str(i))

for i in range(10, 100):
	scrape("0"+str(i))

for i in range(100, 3000):
	scrape(i)

print file_paths

with open('scp_paths.txt', 'w') as outfile:
	json.dump(file_paths, outfile)



