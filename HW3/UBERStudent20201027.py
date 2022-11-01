#!/usr/bin/python3

import sys
import calendar 

input = sys.argv[1]
output = sys.argv[2]

dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'] 
vdic = dict()
tdic = dict()
# uber.txt 읽어오기

with open(input) as datafile:
	data = datafile.read()

	rows = data.split('\n')
	for row in rows:
		dataList = row.split(',')
		base = dataList[0]
		year = int(dataList[1].split('/')[2])	
		month = int(dataList[1].split('/')[0])
		day = int(dataList[1].split('/')[1]) 
		
		date = calendar.weekday(year,month,day)

		vehicles = int(dataList[2])
		trips = int(dataList[3]) 	
	
		strr = base + "," + dayofweek[date]

		if strr not in vdic:
			vdic[strr] = vehicles 
			tdic[strr] = trips
		else:
			vdic[strr] += vehicles
			tdic[strr] += trips
 
file = open(output, "wt")
for strr in vdic:
	file.write(strr + " " + str(vdic[strr]) + "," +str(tdic[strr]) + "\n") 
file.close()
