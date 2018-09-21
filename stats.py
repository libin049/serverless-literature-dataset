#!/usr/bin/env python3

import json
import os
import urllib.request
import pybtex.database

analysis_filename = "serverless-literature-analysis.json"
biblio_filename = "serverless-literature-bibliography.json"

f = open(biblio_filename)
biblio = json.load(f)

f = open(analysis_filename)
analysis = json.load(f)

years = {}
for ident in biblio:
	y = biblio[ident]["year"]
	years[y] = years.get(y, 0) + 1

countries = {}
for ident in analysis:
	cs = analysis[ident]["countries"]
	for c in cs:
		countries[c] = countries.get(c, 0) + 1

academic = 0
for ident in analysis:
	a = analysis[ident]["academic"]
	if a:
		academic += 1

f = open("stats.txt", "w")
print("Years:", years, file=f)
print("Countries:", countries, file=f)
print("Ratio academic to industry:", academic, ":", len(analysis) - academic, "=", academic / len(analysis), file=f)
f.close()

print("Written stats to stats.txt.")
