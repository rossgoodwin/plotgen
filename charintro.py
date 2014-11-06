import random
from random import choice as c
import string

import nltk
import en

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

	# sentences = t.split('.')
	# words = [s.split(' ') for s in sentences]

	pos = en.sentence.tag(t)
	wordtag = map(list, zip(*pos))
	words = wordtag[0]
	tags = wordtag[1]

	# find periods
	# periods = []
	# for i in range(len(words)):
	# 	if words[i] in [".", "!", "?"]:
	# 		periods.append(i)
	# periods.insert(0, 0)

	# containsNameList = [0]

	# containsName = False

	for i in range(len(words)):
		#containsName = False

		# if i in periods and containsName:
		# 	containsNameList.append(i)

		# if i in periods:
		# 	containsName = False

		if words[i].lower() == "character" and i > 0:
			words[i-1] = firstName
			words[i] = lastName
			containsName = True

		elif tags[i] == "PRP":
			words[i] = firstName
			containsName = True
		elif tags[i] == "PRP$":
			words[i] = firstName+"\'s"
			cointainsName = True
		elif tags[i] in ["VBD", "VBG", "VBN", "VBZ"]:
			try:
				words[i] = en.verb.past(words[i], person=3)
			except KeyError:
				pass

		elif words[i] == "trope":
			words[i] = "clue"
		elif words[i] == "tropes":
			words[i] = "clues"
		elif words[i] == "Trope":
			words[i] = "Clue"
		elif words[i] == "Tropes":
			words[i] = "Clues"

		else:
			pass

	# trueWords = []
	# for indx in containsNameList:
	# 	trueWords += words[indx:periods[periods.index(indx)+1]]

	punc = [".", ",", ";", ":", "!", "?"]

	for i in range(len(words)):
		if words[i] in punc:
			w = words[i]
			words[i] = '\b'+w

	final_text = " ".join(words)

	index = string.find(final_text, firstName)

	final_text = firstName+" "+lastName+final_text[index+len(firstName):]

	



	return final_text

intros = char_match()

for x, y in intros.iteritems():
	print x
	print y

	print "\n\n"





