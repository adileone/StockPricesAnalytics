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
    except:
        print(words)
        #next(infile)

    b=float(words[2])

    print ( words[0], 100*(b-a)/a, '%')
