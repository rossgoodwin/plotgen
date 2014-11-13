from erowid_experience_paths import *
import random
import en

# character names
charName = "Ross Goodwin"

# choose a random file
path = random.choice(erowidExpPaths)

# open file and get text
f = open(path, 'r')
text = f.read()
f.close()

splitText = text.split('\\vspace{2mm}')
endOfText = splitText[-1]
report = endOfText[:len(endOfText)-15]



print report