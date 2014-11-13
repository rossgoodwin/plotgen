from sys import argv
import random
from random import choice as c
import string
import math

import nltk
import en

from erowid_experience_paths import *
from tropes_character import *
from tropes_setting import *
from firstnames_f import *
from firstnames_m import *
from surnames import *


# TODO:
# [ ] Fix "I'm" and "I'll" problem
# [ ] Add TOC
# [ ] Add Plot Points / Narrative Points / Phlebotinum


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
	# charTropeDict = dict(zip(charNames, tropeText))

	tropes = []
	for t in range(len(charNames)):
		trope = personalize(charNames[t], tropeText[t])
		tropes.append(trope)

	charDrugPaths = random.sample(erowidExpPaths, len(charNames)*5)
	charDrugs = []
	j = 0
	for path in charDrugPaths:
		ff = open(path, 'r')
		drugText = ff.read()
		ff.close()

		splitText = drugText.split('\\vspace{2mm}')
		endOfText = splitText[-1]
		report = endOfText[:len(endOfText)-15]
		chars = [charNames[int(math.floor(j/5))]]+random.sample(charNames, random.randint(0, 3))
		report = personal_trip(chars, report)
		charDrugs.append(report)
		j+=1

	charSettingPaths = random.sample(settingTropeFiles, len(charNames))
	charSettings = []
	k = 0
	for path in charSettingPaths:
		fff = open(path, 'r')
		settingText = fff.read()
		fff.close()
		churs = [charNames[k]]+random.sample(charNames, random.randint(0, 3))
		setting = personal_trip(churs, settingText)
		charSettings.append(setting)
		k+=1

	charTropeDict = {}
	for i in range(len(charNames)):
		drugsIndex = i*5
		charTropeDict[charNames[i]] = [tropes[i], charDrugs[drugsIndex:drugsIndex+5], charSettings[i]]

	return charTropeDict


def personal_trip(c, t):
	charCount = len(c)

	nameList1 = c[0].split(' ')
	firstName1 = nameList1[0]
	lastName1 = nameList1[1]

	if charCount > 1:
		nameList2 = c[1].split(' ')
		firstName2 = nameList2[0]
		lastName2 = nameList2[1]

	if charCount > 2:
		nameList3 = c[2].split(' ')
		firstName3 = nameList3[0]
		lastName3 = nameList3[1]

	if charCount > 3:
		nameList4 = c[3].split(' ')
		firstName4 = nameList4[0]
		lastName4 = nameList4[1]

	t = t.split('\n')
	t = ' '.join(t)

	try:
		pos = en.sentence.tag(t)
		wordtag = map(list, zip(*pos))
		words = wordtag[0]
		tags = wordtag[1]

		pronoun_count = 0

		for i in range(len(words)):
			if tags[i] == "PRP":
				if pronoun_count % charCount == 0:
					words[i] = firstName1
				elif pronoun_count % charCount == 1:
					words[i] = firstName2
				elif pronoun_count % charCount == 2:
					words[i] = firstName3		
				elif pronoun_count % charCount == 3:
					words[i] = firstName4			
				pronoun_count += 1
			elif tags[i] == "PRP$":
				if pronoun_count % charCount == 0:
					words[i] = firstName1+"\'s"
				elif pronoun_count % charCount == 1:
					words[i] = firstName2+"\'s"
				elif pronoun_count % charCount == 2:
					words[i] = firstName3+"\'s"		
				elif pronoun_count % charCount == 3:
					words[i] = firstName4+"\'s"	
				pronoun_count += 1
			elif tags[i] in ["VBD", "VBG", "VBN", "VBZ"]:
				try:
					words[i] = en.verb.past(words[i], person=3, negate=False)
				except KeyError:
					pass
			else:
				pass

		punc = [".", ",", ";", ":", "!", "?"]

		for i in range(len(words)):
			if words[i] in punc:
				words[i] = '`'+words[i]

		final_text = " ".join(words)

		final_text = final_text.decode('utf8')
		final_text = final_text.encode('ascii', 'ignore')

		final_text = string.replace(final_text, "\\end{itemize}", "")
		final_text = string.replace(final_text, "\\begin{itemize}", "")
		final_text = string.replace(final_text, "\\end{center}", "")
		final_text = string.replace(final_text, "\\begin{center}", "")
		final_text = string.replace(final_text, "\\ldots", " . . . ")
		final_text = string.replace(final_text, "\\egroup", "")
		final_text = string.replace(final_text, "EROWID", "GOVERNMENT")
		final_text = string.replace(final_text, "erowid", "government")
		final_text = string.replace(final_text, "Erowid", "Government")
	
	except:
		final_text = ""

	return final_text


def personalize(c, t):
	nameList = c.split(' ')
	firstName = nameList[0]
	lastName = nameList[1]

	t = t.split('\n')
	t = ' '.join(t)

	try:
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
	
	except:
		final_text = ""

	return final_text


latex_special_char_1 = ['&', '%', '$', '#', '_', '{', '}']
latex_special_char_2 = ['~', '^', '\\']

outputFile = open("output/"+outputFileName+".tex", 'w')

openingTexLines = ["\\documentclass[12pt]{book}",
				   "\\usepackage{ucs}",
				   "\\usepackage[utf8x]{inputenc}",
				   "\\usepackage{hyperref}",
				   "\\title{"+outputFileName+"}",
				   "\\author{collective consciousness fiction generator\\\\http://rossgoodwin.com/ficgen}",
				   "\\date{\\today}",
				   "\\begin{document}",
				   "\\maketitle"]

closingTexLine = "\\end{document}"

for line in openingTexLines:
	outputFile.write(line+"\n\r")
outputFile.write("\n\r\n\r")

intros = char_match()

for x, y in intros.iteritems():

	outputFile.write("\\chapter{"+x+"}\n\r")

	chapter_type = random.randint(0, 4)
	bonus_drug_trip = random.randint(0, 1)
	trip_count = random.randint(1,4)


	# BLOCK ONE

	if chapter_type in [0, 3]:

		for char in y[0]:
			if char == "`":
				outputFile.seek(-1, 1)
			elif char in latex_special_char_1:
				outputFile.write("\\"+char)
			elif char in latex_special_char_2:
				if char == '~':
					outputFile.write("")
				elif char == '^':
					outputFile.write("")
				elif char == '\\':
					outputFile.write("-")
				else:
					pass
			else:
				outputFile.write(char)

	elif chapter_type in [1, 4]:

		for char in y[2]:
			if char == "`":
				outputFile.seek(-1, 1)
			elif char in latex_special_char_1:
				outputFile.write("\\"+char)
			elif char in latex_special_char_2:
				if char == '~':
					outputFile.write("")
				elif char == '^':
					outputFile.write("")
				elif char == '\\':
					outputFile.write("-")
				else:
					pass
			else:
				outputFile.write(char)

	elif chapter_type == 2:

		for char in y[1][0]:
			if char == "`":
				outputFile.seek(-1, 1)
			else:
				outputFile.write(char)

	outputFile.write("\n\r\n\r\n\r")

	
	# BLOCK TWO

	if chapter_type == 0:

		for char in y[2]:
			if char == "`":
				outputFile.seek(-1, 1)
			elif char in latex_special_char_1:
				outputFile.write("\\"+char)
			elif char in latex_special_char_2:
				if char == '~':
					outputFile.write("")
				elif char == '^':
					outputFile.write("")
				elif char == '\\':
					outputFile.write("-")
				else:
					pass
			else:
				outputFile.write(char)

	elif chapter_type == 1:

		for char in y[0]:
			if char == "`":
				outputFile.seek(-1, 1)
			elif char in latex_special_char_1:
				outputFile.write("\\"+char)
			elif char in latex_special_char_2:
				if char == '~':
					outputFile.write("")
				elif char == '^':
					outputFile.write("")
				elif char == '\\':
					outputFile.write("-")
				else:
					pass
			else:
				outputFile.write(char)

	elif chapter_type in [3, 4]:

		for char in y[1][0]:
			if char == "`":
				outputFile.seek(-1, 1)
			else:
				outputFile.write(char)

	elif chapter_type == 2 and bonus_drug_trip:

		for tripIndex in range(trip_count):

			for char in y[1][tripIndex+1]:
				if char == "`":
					outputFile.seek(-1, 1)
				else:
					outputFile.write(char)

	else:
		pass

	outputFile.write("\n\r\n\r\n\r")


	# BLOCK THREE

	if chapter_type in [0, 1, 3, 4] and bonus_drug_trip:

		for tripIndex in range(trip_count):

			for char in y[1][tripIndex+1]:
				if char == "`":
					outputFile.seek(-1, 1)
				else:
					outputFile.write(char)

		outputFile.write("\n\r\n\r\n\r")

	else:
		pass


outputFile.write("\n\r\n\r")
outputFile.write(closingTexLine)


outputFile.close()


print '\"output/'+outputFileName+'.tex\"'