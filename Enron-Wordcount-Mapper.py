#!/usr/bin/env python
import sys
import dateutil.parser
import datetime

for line in sys.stdin:
	#timestamp,sender,recipient = line.split()  #gives an error for large-etl file-'ValueError: too many values to unpack'
	#if (len(words) > 3): print words
	words = line.split()
	timestamp = dateutil.parser.parse(words[0],ignoretz=True)
	sender = words[1]
	recipient = words[2]
	if (	(datetime.datetime(2001,9,5) < timestamp < datetime.datetime(2001,9,9))
		and ('@enron' in sender)
		and (not '@enron' in recipient)
		):
	#   print timestamp.strftime("%B %d, %Y") + "\t" + sender + "\t" + recipient
		print sender + "\t1"