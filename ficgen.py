import argparse
import random
from random import choice as rc
from random import sample as rs
from random import randint as ri
import string
import math

import nltk
import en

from erowid_experience_paths import erowidExpPaths
from tropes_character import characterTropeFiles
from tropes_setting import settingTropeFiles
from scp_paths import scpPaths
from firstnames_f import fFirstNames
from firstnames_m import mFirstNames
from surnames import surnames


# TODO:
# [ ] CLEAN UP TROPE FILE PATHS LIST
# [ ] Fix "I'm" and "I'll" problem
# [ ] Add Plot Points / Narrative Points / Phlebotinum
# [ ] subtrope / sub-trope
# [ ] add yelp reviews
# [ ] add livejournal
# [ ] add SCP


# Argument Values

genre_list = ['literary', 'sci-fi', 'fantasy', 'history', 'romance', 'thriller', 
			  'mystery', 'crime', 'pulp', 'horror', 'beat', 'fan', 'western', 
			  'action', 'war', 'family', 'humor', 'sport', 'speculative']
conflict_list = ['nature', 'man', 'god', 'society', 'self', 'fate', 'tech', 'no god', 'reality', 'author']
narr_list = ['first', '1st', '1', 'third', '3rd', '3', 'alt', 'alternating', 'subjective', 
			 'objective', 'sub', 'obj', 'omniscient', 'omn', 'limited', 'lim']

# In GUI, use logarithmic sliders for charcount, length, and other sliders as necessary
parser = argparse.ArgumentParser(description='Story Parameters')
parser.add_argument('--charnames', nargs='*', help="Character Names")
parser.add_argument('--title', help="Story Title")
parser.add_argument('--length', help="Story Length (0-999)", type=int)
parser.add_argument('--charcount', help="Character Count (0-999)", type=int)
parser.add_argument('--genre', nargs='*', help="Genre", choices=genre_list)
parser.add_argument('--conflict', nargs='*', help="Conflict", choices=conflict_list)
parser.add_argument('--passion', help="Passion (0-999)", type=int)
parser.add_argument('--verbosity', help="Verbosity (0-999)", type=int)
parser.add_argument('--realism', help="Realism (0-999)", type=int)
parser.add_argument('--density', help="Density (0-999)", type=int)
parser.add_argument('--accessibility', help="Accessibility (0-999)", type=int)
parser.add_argument('--depravity', help="Depravity (0-999)", type=int)
parser.add_argument('--linearity', help="Linearity (0-999)", type=int)
parser.add_argument('--narrator', nargs='*', help="Narrative PoV", choices=narr_list)
args = parser.parse_args()



# ESTABLISH SYSTEM-WIDE COEFFICIENTS/CONSTANTS

# tsv = trope setting volume
# GET THIS INTO THE NOVEL CLASS
TSV = (args.length/2.0 + args.realism/6.0 + args.passion/3.0)/1000
if 'fan' in args.genre:
	TSV += 1.0
TSV = int(5.0*TSV)
TSV += 1
print TSV

CC = args.charcount/2


# file text fetcher
def get_file(fp):

	f = open(fp, 'r')
	t = f.read()
	f.close()

	return t



# CLASSES

class Character(object):

	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName
		self.introDesc = ""
		self.scenes = []
		self.friends = []



class Novel(object):

	def __init__(self):
		# Note that character argvs are used in
		# Character class above. They are not
		# used in this class.
		self.argvalues = args

	# Characters

	def make_chars(self):
		# establish gender ratio
		charGenders = [ri(0,1) for _ in range(CC)]
		
		# initialize list of characters
		chars = []

		# add user defined characters
		for firstlast in args.charnames:
			fl_list = firstlast.split('_')  # Note that split is an underscore!
			chars.append(Character(fl_list[0], fl_list[1]))

		# add generated characters
		for b in charGenders:
			if b:
				chars.append(Character(rc(fFirstNames), rc(surnames)))
			else:
				chars.append(Character(rc(mFirstNames), rc(surnames)))

		# establish list of intro scenes
		introScenePaths = rs(characterTropeFiles, len(chars))

		# establish list of settings
		settings = rs(settingTropeFiles, len(chars)*TSV)

		i = 0
		j = 0
		for c in chars:

			# make friends
			c.friends += rs(chars, ri(1,len(chars)-1))
			if c in c.friends:
				c.friends.remove(c)

			# add introduction description
			c.introDesc = self.personal_trope([c], introScenePaths[i])

			# add scenes -- maybe adjust that number (TSV)
			for k in range(TSV):
				c.scenes.append(self.personal_trope(chars, settings[j+k]))

			i += 1
			j += TSV


		return chars


	def personal_trope(self, charList, filePath):
		text = get_file(filePath)
		# text = text.decode('utf8')
		# text = text.encode('ascii', 'ignore')

		if len(charList) == 1:
			characterTrope = True
		else:
			characterTrope = False

		try:

			pos = en.sentence.tag(text)
			wordtag = map(list, zip(*pos))
			words = wordtag[0]
			tags = wordtag[1]

			for i in range(len(words)):
				charRef = rc(charList)
				if words[i].lower() == "character" and i > 0:
					words[i-1] = charRef.firstName
					words[i] = charRef.lastName
					containsName = True

				elif tags[i] == "PRP":
					words[i] = charRef.firstName
					containsName = True
				elif tags[i] == "PRP$":
					words[i] = charRef.firstName+"\'s"
					cointainsName = True
				elif tags[i] in ["VBD", "VBG", "VBN", "VBZ"]:
					try:
						words[i] = en.verb.past(words[i], person=3, negate=False)
					except:
						pass

				if characterTrope:

					if words[i] == "have":
						words[i] = "has"
					elif words[i] == "are":
						words[i] = "is"

			punc = [".", ",", ";", ":", "!", "?"]

			for i in range(len(words)):
				if words[i] in punc:
					words[i] = '\b'+words[i]

			final_text = " ".join(words)

			if characterTrope:

				mainCharRef = rc(charList)

				index = string.find(final_text, mainCharRef.firstName)

				if final_text[index+len(mainCharRef.firstName)+1:index+len(mainCharRef.firstName)+1+len(mainCharRef.lastName)] == mainCharRef.lastName:
					final_text = final_text[index:]
				else:
					final_text = mainCharRef.firstName+" "+mainCharRef.lastName+final_text[index+len(mainCharRef.firstName):]

			final_text = string.replace(final_text, "trope", "clue")
			final_text = string.replace(final_text, "Trope", "clue")
			final_text = string.replace(final_text, "TROPE", "CLUE")

		except:
			final_text = ""


		return final_text


	def print_chars(self):

		c = self.make_chars()
		for character in c:
			print 'INTRO DESC'
			print '\n\n'
			print character.introDesc
			print '\n\n'
			print 'SCENES'
			print '\n\n'
			for s in character.scenes:
				print s
			print '\n\n'






foobar = Novel()
foobar.print_chars()





# GENERAL FUBAR AREA

# def build_wireframe():
# 	if bool(args.length):
# 		chapterCount = int(args.length/10)
# 	else:
# 		chapterCount = random.randint
# 	chapters = [smp(range(100), ri(1, 15)) for _ in range(chapterCount)]




