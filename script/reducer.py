#!/usr/bin/env python
import sys

infile = sys.stdin

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    words = line.split(' ')

    try:
        a=float(words[1])
        b=float(words[2])
        print('{} {}%').format(words[0], round(100*(b-a)/a, 2))
    
    except ValueError as err:
        print(words, err)

