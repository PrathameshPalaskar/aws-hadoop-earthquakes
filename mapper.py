#!/usr/bin/env python

import csv
import sys

#with open('all_month.csv', 'rb') as csvfile:
#	spamreader = csv.reader(csvfile)
#	spamreader.next()
#	for row in spamreader:

#this step enables us to skip the header
infile =sys.stdin
next(infile)

#mapper function starts 
for line in infile:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    row = line.split(',')
    date = row[0][:-14]
    # increase counters
    if row[4] == '':
	print'%s\t%s\t%s\t%s' %(date,-1, 0 ,1)
    else:
        #dividing the magnitude in ranges
	magni = float(row[4])
	if magni < 0:
		print'%s\t%s\t%s\t%s\t' %(date,magni, 0, 1)
	elif 0 <= magni < 1:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 1, 1)
	elif 1 <= magni < 2:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 2, 1)
	elif 2 <= magni < 3:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 3, 1)
	elif 3 <= magni < 4:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 4, 1)
	elif 4 <= magni < 5:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 5, 1)
	elif 5 <= magni < 6:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 6, 1)
	elif 6 <= magni < 7:
		print '%s\t%s\t%s\t%s\t' %(date,magni, 7, 1)

