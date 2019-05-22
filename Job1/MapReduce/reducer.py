#!/usr/bin/env python2
import sys

infile = sys.stdin

check = dict()
volumes = dict()
myDict = {}

#get input lines from stdin
for line in infile:
    
    #remove spaces from beginning and end of the line
    line = line.strip()

    #split it into words
    words = line.split(' ')

    if words[0] not in check.keys():
        check[words[0]]=[]
    
    check[words[0]].append(float(words[1]))

    if words[0] not in volumes.keys():
        volumes[words[0]]=[]
    
    volumes[words[0]].append(float(words[2]))


for key in check.keys():

    try:
        a=check[key][0]
        b=check[key][-1]

        if key not in myDict.keys():
            myDict[key]=[]
    
        myDict[key].append(round(100*(b-a)/a, 2))
        myDict[key].append(min(check[key]))
        myDict[key].append(max(check[key]))
        myDict[key].append(sum(volumes[key]) / len(volumes[key]))
    
    except ValueError as err:
        print(words, err)    
 
sorted_by_value = sorted(myDict.items(), key = lambda kv:(kv[1], kv[0]))
sorted_by_value.reverse()

for elementoLista in sorted_by_value[:10]:
    print "{}\tincremento: {}%\tmin: {}\tmax: {}\tavg: {}".format(elementoLista[0],
                                                            elementoLista[1][0],
                                                            round(elementoLista[1][1],4),
                                                            round(elementoLista[1][2],3), 
                                                            round(elementoLista[1][3],2))