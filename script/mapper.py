#!/usr/bin/env python2
import sys
from datetime import datetime as dt

check = dict()

infile = sys.stdin

#skip first line of input file
next(infile)

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    words = line.split(',')

    date = dt.strptime(words[7], "%Y-%m-%d")
    start = dt.strptime("1998-01-01", "%Y-%m-%d")
    end = dt.strptime("2018-01-01", "%Y-%m-%d")


    if ((date > start) and (date < end)):
        print "{} {} {}".format(words[0], words[2], words[6])