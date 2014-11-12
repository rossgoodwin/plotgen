from sys import argv
import random
from random import choice as c
import string

import nltk
import en

from tropes_character import *
from firstnames_f import *
from firstnames_m import *
from surnames import *


script, outputFileName, inputCharName = argv


def name_chars():
	charNo = random.randint(7,51)
	charGenders = [random.randint(0,1) for _ in range(charNo)]
	charNames = [inputCharName]
	for i in charGenders:
		if charGenders[i]:
			charNames.append(c(fFirstNames)+" "+c(surnames))
		else:
			charNames.append(c(mFirstNames)+" "+c(surnames))
	return charNames


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
	nameList = c.split(' ')
	firstName = nameList[0]
	lastName = nameList[1]

	t = t.split('\n')
	t = ' '.join(t)

	pos = en.sentence.tag(t)
	wordtag = map(list, zip(*pos))
	words = wordtag[0]
	tags = wordtag[1]

	for i in range(len(words)):
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
				words[i] = en.verb.past(words[i], person=3, negate=False)
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
		elif words[i] == "have":
			words[i] = "has"
		elif words[i] == "are":
			words[i] = "is"

		else:
			pass


	punc = [".", ",", ";", ":", "!", "?"]

	for i in range(len(words)):
		if words[i] in punc:
			words[i] = '`'+words[i]

	final_text = " ".join(words)

	index = string.find(final_text, firstName)

	if final_text[index+len(firstName)+1:index+len(firstName)+1+len(lastName)] == lastName:
		final_text = final_text[index:]
	else:
		final_text = firstName+" "+lastName+final_text[index+len(firstName):]

	final_text = final_text.decode('utf8')
	final_text = final_text.encode('ascii', 'ignore')

	return final_text


latex_special_char_1 = ['&', '%', '$', '#', '_', '{', '}']
latex_special_char_2 = ['~', '^', '\\']

outputFile = open("output/"+outputFileName+".tex", 'w')

openingTexLines = ["\\documentclass[12pt]{book}",
				   "\\title{"+outputFileName+"}",
				   "\\author{collective consciousness fiction generator\\\\http://rossgoodwin.com/ficgen}",
				   "\\date{\\today}",
				   "\\begin{document}",
				   "\\maketitle"]

closingTexLine = "\\end{document}"

for line in openingTexLines:
	outputFile.write(line+"\n")
outputFile.write("\n\n")

intros = char_match()

for x, y in intros.iteritems():

	outputFile.write("\\chapter{"+x+"}\n")

	# for char in x:
	# 	if char == "`":
	# 		outputFile.seek(-1, 1)
	# 	else:
	# 		outputFile.write(char)

	# outputFile.write("\n")

	for char in y:
		if char == "`":
			outputFile.seek(-1, 1)
		elif char in latex_special_char_1:
			outputFile.write("\\"+char)
		elif char in latex_special_char_2:
			if char == '~':
				outputFile.write("\\textasciitilde")
			elif char == '^':
				outputFile.write("\\textasciicircum")
			elif char == '\\':
				outputFile.write("\\textbackslash")
			else:
				pass
		else:
			outputFile.write(char)

	outputFile.write("\n\n")


outputFile.write("\n\n")
outputFile.write(closingTexLine)


outputFile.close()


print '\"output/'+outputFileName+'.tex\"'





