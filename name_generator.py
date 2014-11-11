from random import choice as c

from firstnames_f import *
from firstnames_m import *
from surnames import *

firstnames = mFirstNames + fFirstNames

for _ in range(25):
	print c(firstnames) + " " + c(surnames)