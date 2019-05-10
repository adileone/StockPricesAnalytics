#!/usr/bin/env python2
import sys
from datetime import datetime as dt
import string

infile = sys.stdin

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker,close,data,sector = line.split('\t')

    date = dt.strptime(data, "%Y-%m-%d")
    start = dt.strptime("2015-01-01", "%Y-%m-%d")
    end= dt.strptime("2018-12-31", "%Y-%m-%d")

    if ((date >= start) and (date <= end)) and sector != 'N/A':

        print "{}|{}|{}|{}".format(ticker,close,date.year,sector)  