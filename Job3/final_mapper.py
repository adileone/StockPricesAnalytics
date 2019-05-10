#!/usr/bin/env python2
import sys

check={}

infile = sys.stdin

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker,year,sector,percentage = line.split('|')

    if (year == '2015') :
        continue

    print "{}|{}|{}".format(ticker,percentage,sector)    
