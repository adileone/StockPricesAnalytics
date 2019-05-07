#!/usr/bin/env python2
import sys

infile = sys.stdin

last_ticker = None

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker, close, volume, data, sector = line.split('|')

    if sector != '-':
        last_ticker=ticker
        last_sector=sector
        continue
    
    print "{}\t{}\t{}\t{}\t{}".format(last_ticker,close,volume,data,last_sector)




        
        

        