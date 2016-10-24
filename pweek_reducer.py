#!/usr/bin/env python
import sys
from operator import itemgetter

current_group = None
current_count = 0
current_week = None

#this is the output which serves as input to the reducer
for line in sys.stdin:
	# remove leading and trailing whitespace
	line1 = line.strip()
	
	# parse the input we got from mapper.py
	week,group,count = line.split('\t',2)
	
	# convert count (currently a string) to int
	try:
		count = float(count)
	
	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        	continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
	if current_week == week and current_group == group:
		current_count += count
	
	else:
		if current_week  and current_group:
            # write result to STDOUT
			print '%s\t%s\t%s' % (current_week,current_group,current_count)
		current_count = count
		current_group = group
		current_week = week 

# do not forget to output the last word if needed!
if current_group == group and current_week == week:
	print '%s\t%s\t%s' % (current_week,current_group,current_count)	





	




