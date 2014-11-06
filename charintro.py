import random
from random import choice as c
import string

import nltk

from tropes_character import *
from firstnames_f import *
from firstnames_m import *
from surnames import *

def name_chars():
	charNo = random.randint(3,9)
	charGenders = [random.randint(0,1) for _ in range(charNo)]
	charNames = []
	for i in charGenders:
		if charGenders[i]:
			charNames.append(c(fFirstNames)+" "+c(surnames))
		else:
			charNames.append(c(mFirstNames)+" "+c(surnames))
	return charNames

# for _ in range(10):
# 	char_names = name_chars()
# 	for name in char_names:
# 		print name
# 	print "\n\n"

def char_match():
	charNames = name_chars()
	charTropes = random.sample(characterTropeFiles, len(charNames))
	tropeText = []
	for tropePath in charTropes:
		f = open(tropePath, 'r')
		tropeText.append(f.read())
		f.close()
	charTropeDict = dict(zip(charNames, tropeText))
	for char, trope in charTropeDict.iteritems():
		charTropeDict[char] = personalize(char, trope)
	return charTropeDict

def personalize(c, t):
	pronouns = ['he', 'she', 'they', 'him', 'her', 'them']
	pronouns_possessive = ['his', 'hers', 'their', 'theirs', "he's", "she's", "they're"]

	nameList = c.split(' ')
	firstName = nameList[0]
	lastName = nameList[1]

	t = t.split('\n')
	t = ' '.join(t)

	sentences = t.split('.')
	words = [s.split(' ') for s in sentences]

	for i in range(len(words)):
		containsName = False
		for j in range(len(words[i])):
			if words[i][j].lower() == "character" and j > 0:
				words[i][j-1] = firstName
				words[i][j] = lastName
				containsName = True
			elif words[i][j].lower() == "trope":
				words[i][j] = "clue"
			elif words[i][j].lower() == "tropes":
				words[i][j] = "clues"
			elif words[i][j] in pronouns:
				words[i][j] = firstName
				containsName = True
			elif words[i][j] in pronouns_possessive:
				words[i][j] = firstName+"\'s"
				containsName = True
		if not containsName:
			words[i] = ['\b']

	ws = list(string.whitespace)
	ws.append("")
	punc = list(string.punctuation)
	wsPunc = ws+punc

	final_text_list = [" ".join(w) for w in words if not w in wsPunc]
	if final_text_list[0] in wsPunc:
		final_text_list = final_text_list[1:]

	final_text = ".".join(final_text_list)

	# for i in range(len(final_text)-len(firstName)):
	# 	firstMatch = False
	# 	for j in range(len(firstName)):
	# 		if firstName[j] == final_text[i+j]:
	# 			firstMatch = True
	# 		else:
	# 			firstMatch = False
	# 	if firstMatch:
	# 		index = i
	# 		break

	index = string.find(final_text, firstName)

	final_text = final_text[index:]

	return final_text

intros = char_match()

for x, y in intros.iteritems():
	print x
	print y

	print "\n\n"





