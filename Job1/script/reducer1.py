#!/usr/bin/env python2
import sys

infile = sys.stdin

myDict = {}

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    ticker, firstClose, lastClose, minimumPrice, maximumPrice, avg_volume = line.split(' ')
    words = ticker, firstClose, lastClose, minimumPrice, maximumPrice, avg_volume; 

    try:
        a=float(firstClose)
        b=float(lastClose)

        if ticker not in myDict.keys():
            myDict[ticker]=[]
    
        myDict[ticker].append(round(100*(b-a)/a, 2))
        myDict[ticker].append(minimumPrice)
        myDict[ticker].append(maximumPrice)
        myDict[ticker].append(avg_volume)
                      
    except ValueError as err:
        print(words, err)


sorted_by_value = sorted(myDict.items(), key = lambda kv:(kv[1], kv[0]))
sorted_by_value.reverse()

for el in sorted_by_value[:10]:
    print "{}\t{}%\t{}\t{}\t{}".format(el[0], el[1][0], el[1][1], el[1][2], el[1][3])



