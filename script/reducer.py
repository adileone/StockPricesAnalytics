#!/usr/bin/env python2
import sys

infile = sys.stdin

myDict = {}

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    words = line.split(' ')

    try:
        a=float(words[1])
        b=float(words[2])
        myDict[words[0]] = round(100*(b-a)/a, 2)
        
    
    except ValueError as err:
        print(words, err)


sorted_by_value = sorted(myDict.items(), key = lambda kv:(kv[1], kv[0]))
sorted_by_value.reverse()
for el in sorted_by_value[:10]:
    print "{}\t{}%".format(el[0],el[1])



