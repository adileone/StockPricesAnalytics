#!/usr/bin/env python2
import sys

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

    if words[0] not in check.keys():
        check[words[0]]=[]
    
    check[words[0]].append(words[2])

for key in check.keys():
    print "{} {} {}".format(key, check[key][0], check[key][-1])
