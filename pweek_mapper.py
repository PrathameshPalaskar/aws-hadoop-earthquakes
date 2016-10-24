#!/usr/bin/env python

import csv
import sys
import datetime

#with open('all_month.csv', 'rb') as csvfile:
#	spamreader = csv.reader(csvfile)
#	spamreader.next()
#	for row in spamreader:

infile =sys.stdin
next(infile)

for line in infile:
    # remove leading and trailing whitespace
	line = line.strip()
    # split the line into words
	row = line.split(',')
	date = row[0][:-14]
	date_format = datetime.datetime.strptime(date,"%Y-%m-%d").date()
    #get the week number
	week_number = date_format.isocalendar()[1]

    # increase counters
	if row[4] == '':
		print'%s\t%s\t%s\t' %(week_number,0 ,1)
	else:
		magni = float(row[4])
		if magnini < 0:
			print'%s\t%s\t%s\t' %(week_number,0, 1)
		elif 0 <= magnini < 1:
			print '%s\t%s\t%s\t' %(week_number,1, 1)
		elif 1 <= magni < 2:
			print '%s\t%s\t%s\t' %(week_number,2, 1)
		elif 2 <= magni < 3:
			print '%s\t%s\t%s\t' %(week_number,3, 1)
		elif 3 <= magni < 4:
			print '%s\t%s\t%s\t' %(week_number,4, 1)
		elif 4 <= magni < 5:
			print '%s\t%s\t%s\t' %(week_number,5, 1)
		elif 5 <= magni < 6:
			print '%s\t%s\t%s\t' %(week_number,6, 1)
		elif 6 <= magni < 7:
			print '%s\t%s\t%s\t' %(week_number,7, 1)


