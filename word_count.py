from tropes_character import *

tropeText = ""

for tropePath in characterTropeFiles:
	try:
		f = open(tropePath, 'r')
		tropeText += ("\n" + f.read())
		f.close()
	except IOError:
		pass

tropeTokens = tropeText.split(" ")

print len(tropeTokens)

