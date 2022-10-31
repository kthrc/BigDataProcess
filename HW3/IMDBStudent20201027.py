#!/usr/bin/python3

import sys

input = sys.argv[1]
output = sys.argv[2] 

# movies 읽어오기

with open(input) as datafile:

	data = datafile.read()
	
	rows = data.split('\n')
	dic = {}	
	
	for row in rows:
		genreList = row.split('::')[2]
		genre = genreList.split('|')

		for i in genre:
			if i not in dic:
				dic[i] = 1
			else:
				dic[i] += 1	
	
file = open(output, "wt")
for key, value in dic.items():
	file.write(key + " " + str(value) + "\n")

file.close() 
