import os
import json

sysPath = "/Users/rg/Projects/plotgen/gutenberg/www.gutenberg.lib.md.us/"

gPaths = {}

for root, dirs, files in os.walk(sysPath):
    for f in files:
        if f.endswith(".zip") and not (f.endswith("-8.zip") or f.endswith("-0.zip")):
        	fname = f.split(".")[0]
        	gPaths[fname] = os.path.join(root, f)

j = json.dumps(gPaths)

ff = open("/Users/rg/Projects/plotgen/ficgen/g_paths.json", 'w')

print >> ff, j

ff.close()